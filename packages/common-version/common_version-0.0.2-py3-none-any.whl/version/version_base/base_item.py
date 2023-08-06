# -*- coding: utf-8 -*-
import copy


# from version import PackageType


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        start = self.start
        end = self.end
        if not start:
            start = "0"
        if not end:
            end = "9999999"
        return f"{start},{end}"

    def in_line(self, spot, is_end=True):
        from version import get_base_version
        """
        判断是否在范围内
        :param spot:
        :return:
        """
        is_in_line = False
        start = self.start
        end = self.end
        if not self.start:
            start = "0"
        if not self.end:
            end = "99999999"
        if not spot:
            if is_end:
                spot = "99999999"
            else:
                spot = "0"
        left_flag = get_base_version(version_name=start, package_type="snyk").__cmp__(spot)
        right_flag = get_base_version(version_name=end, package_type="snyk").__cmp__(spot)
        if left_flag <= 0 and right_flag >= 0:
            is_in_line = True
        return is_in_line


class ItemBase:
    def merge_and(self, other):
        raise NotImplementedError

    def merge_or(self, other):
        raise NotImplementedError

    def is_valid(self):
        return True


class Item(ItemBase):
    def __init__(
            self, left=None, right=None, left_open=None, right_open=None, valid=True
    ):
        self.left = left
        self.right = right
        self.left_open = left_open
        self.right_open = right_open
        self.valid = self.set_valid(valid)

    def compare_left(self, part_left_flag):
        if part_left_flag == -1:
            final_flag = True
        elif (part_left_flag == 0 or part_left_flag == "0") and self.left_open:
            final_flag = True
        else:
            final_flag = False
        return final_flag

    def compare_is_in(self, part_left_flag):
        if part_left_flag == -1:
            final_flag = False
        elif part_left_flag == 0 and self.left_open:
            final_flag = True
        else:
            final_flag = False
        return final_flag

    def compare_right(self, part_right_flag):
        if part_right_flag == 1:
            right_flag = True
        elif part_right_flag == 0 and self.right_open:
            right_flag = True
        else:
            right_flag = False
        return right_flag

    def is_in_version_item(self, other, package_type):
        from version.version_base import Equal_Not_Compare_Type, Equal_Or_Compare_Type
        from version import get_base_version, change_to_expression
        if self.left == self.right and package_type in Equal_Not_Compare_Type:
            if self.left == other or self.right == other:
                return True
            else:
                return False
        elif self.left == self.right and package_type in Equal_Or_Compare_Type:
            if self.right == other:
                final_flag = True
                return final_flag
            else:
                try:
                    if package_type != "cargo":
                        left_version = change_to_expression(package_type=package_type, version_expression=other)
                    else:
                        left_version_obj = get_base_version(package_type=package_type, version_name=other)
                        left_version = Item(left_open=True, right_open=True, left=left_version_obj.new_version,
                                            right=left_version_obj.new_version)
                    if left_version.left == left_version.right:
                        version1 = get_base_version(package_type=package_type, version_name=other)
                        flag = version1.__cmp__(self.left)
                        return True if flag == 0 else False
                    return False
                except Exception:
                    return False
        else:
            if self.left:
                left_version = get_base_version(package_type=package_type, version_name=self.left)
                try:
                    part_left_flag = left_version.__cmp__(other)
                except Exception:
                    return False
            else:
                part_left_flag = -1
            if self.right:
                right_version = get_base_version(package_type=package_type, version_name=self.right)
                try:
                    part_right_flag = right_version.__cmp__(other)
                except Exception:
                    return False
            else:
                part_right_flag = 1
            left_flag = self.compare_left(part_left_flag)
            right_flag = self.compare_right(part_right_flag)
            return left_flag and right_flag

    def is_valid(self):
        return self.valid

    def set_valid(self, valid):
        from version import get_base_version
        valid = valid
        if self.right and self.left:
            if self.left != self.right:
                is_intersect = get_base_version(version_name=self.left).__cmp__(self.right)
                if is_intersect > 0:
                    valid = False
        return valid

    def __str__(self):
        return self.get_value()

    def get_value(self):
        """
        返回单个表达式
        :return:
        """
        left = self.left
        right = self.right
        if not self.valid:
            return "NONE"
        if not left:
            left = ""
        if not right:
            right = ""
        if left == "" and right == "":
            return "*"
        if left == right and self.right_open and self.left_open and left:
            return str(left)
        if left == right and (not self.right_open and not self.left_open) and left:
            return "-"
        if left is None and right is None:
            return "*"
        if self.right_open:
            right_identifier = "]"
        else:
            right_identifier = ")"
        if self.left_open:
            left_identifier = "["
        else:
            left_identifier = "("
        return left_identifier + left + "," + right + right_identifier

    def merge_and(self, other):
        """
        且表达式合并
        :param other:
        :return:
        """
        if isinstance(other, ItemGroup):
            return other.merge_and(self)
        new_item = self.is_intersect(other, is_or=False)
        return new_item

    def merge_or(self, other):
        """
        或表达式合并
        :param other:
        :return:
        """
        if isinstance(other, ItemGroup):
            return other.merge_or(self)
        new_item = self.is_intersect(other, is_or=True)
        return new_item

    def sort_match_line(self, first_line, other_line):
        from version import sort_versions
        if not first_line.start:
            first_line.start = "0"
        if not other_line.start:
            other_line.start = "0"
        if not first_line.end:
            first_line.end = "99999999"
        if not other_line.end:
            other_line.end = "99999999"
        version_list = [
            first_line.start,
            first_line.end,
            other_line.start,
            other_line.end,
        ]
        sort_list, _ = sort_versions(versions=version_list, remove_not_final=False)
        return sort_list

    def is_open(self, other, version_str, is_left=False, is_or=False, is_null=False):
        """
        判断开闭区间
        :param is_left: 是否是左边
        :param is_or: 是否是或
        :param is_null: 当为左边时，左边是否为空或0 ，当为右边时同理
        :param other:
        :param version_str:
        :return:
        """
        if is_left:
            if is_null:
                if self.left == version_str:
                    return self.left_open
                else:
                    return other.left_open
            else:
                if self.left == version_str or other.left == version_str:
                    if is_or:
                        if self.left_open or other.left_open:
                            return True
                    else:
                        if self.left_open and other.left_open:
                            return True
        else:
            if is_null:
                if self.right == version_str:
                    return self.right_open
                else:
                    return other.right_open
            else:
                if self.right == version_str or other.right == version_str:
                    if is_or:
                        if self.right_open or other.right_open:
                            return True
                    else:
                        if self.right_open and other.right_open:
                            return True
        return False

    def is_open2(self, other, version_str, is_left):
        if is_left:
            if other.left == version_str:
                return other.left
            else:
                return self.left

    def is_intersect2(self, other, is_or=False):
        """
        两个item判断是否相交，16种情况
        @param other:
        @param is_or:
        @return:
        """
        first_line = Line(start=self.left, end=self.right)
        other_line = Line(start=other.left, end=other.right)
        other_start_is_in_first = first_line.in_line(other_line.start, is_end=False)  # 4
        other_end_is_in_first = first_line.in_line(other_line.end)  # 5
        first_start_is_in_other = other_line.in_line(first_line.start, is_end=False)  # 6
        first_end_is_in_other = other_line.in_line(first_line.end)  # 7
        # sort_list = self.sort_match_line(first_line, other_line)
        # sort_list = [i if i != "0" else "" for i in sort_list]
        # sort_list = [i if i != "99999999" else "" for i in sort_list]
        new_item = Item(valid=False)
        if is_or:
            if not other_start_is_in_first and not other_end_is_in_first and \
                    not first_start_is_in_other and not first_end_is_in_other:
                new_item = ItemGroup(self, other, is_or=is_or)
            elif not other_start_is_in_first and not other_end_is_in_first and \
                    not first_start_is_in_other and first_end_is_in_other:
                new_item = Item(
                    left_open=self.left_open,
                    right_open=other.right_open,
                    left=self.left,
                    right=other.right
                )
            elif not other_start_is_in_first and not other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                new_item = copy.deepcopy(other)
            elif not other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and not first_end_is_in_other:
                new_item = Item(
                    left_open=other.left_open,
                    right_open=self.right_open,
                    left=other.left,
                    right=self.right
                )
            elif not other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                right_open = self.right_open or other.right_open
                new_item = Item(
                    left_open=other.left_open,
                    right_open=right_open,
                    left=other.left,
                    right=other.right
                )
            elif other_start_is_in_first and not other_end_is_in_first and \
                    not first_start_is_in_other and first_end_is_in_other:
                if not self.right_open and not other.left_open:
                    new_item = ItemGroup(self, other, is_or=True)
                else:
                    new_item = Item(
                        left_open=self.left_open,
                        right_open=other.right_open,
                        left=self.left,
                        right=other.right
                    )
            elif other_start_is_in_first and not other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                left_open = self.left_open or other.left_open
                new_item = Item(
                    left_open=left_open,
                    right_open=other.right_open,
                    left=other.left,
                    right=other.right
                )
            elif other_start_is_in_first and other_end_is_in_first and \
                    not first_start_is_in_other and not first_end_is_in_other:
                new_item = copy.deepcopy(self)
            elif other_start_is_in_first and other_end_is_in_first and \
                    not first_start_is_in_other and first_end_is_in_other:
                right_open = self.right_open or other.right_open
                new_item = Item(
                    left_open=self.left_open,
                    right_open=right_open,
                    left=self.left,
                    right=self.right
                )
            elif other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and not first_end_is_in_other:
                left_open = self.left_open or other.left_open
                new_item = Item(
                    left_open=left_open,
                    right_open=self.right_open,
                    left=self.left,
                    right=self.right
                )
            elif other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                left_open = self.left_open or other.left_open
                right_open = self.right_open or other.right_open
                new_item = Item(
                    left_open=left_open,
                    right_open=right_open,
                    left=self.left,
                    right=self.right
                )
        else:
            if not other_start_is_in_first and other_end_is_in_first and not \
                    first_start_is_in_other and first_end_is_in_other:
                if self.right_open and other.right_open:
                    new_item = Item(
                        left_open=True,
                        right_open=True,
                        left=self.right,
                        right=self.right
                    )
            elif not other_start_is_in_first and not other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                new_item = copy.deepcopy(self)
            elif not other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                right_open = self.right_open and other.right_open
                new_item = Item(
                    left_open=self.left_open,
                    right_open=right_open,
                    left=self.left,
                    right=self.right
                )
            elif other_start_is_in_first and not other_end_is_in_first and \
                    first_start_is_in_other and not first_end_is_in_other:
                if self.left_open and other.left_open:
                    new_item = Item(
                        left_open=True,
                        right_open=True,
                        left=self.left,
                        right=self.left
                    )
            elif other_start_is_in_first and not other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                if self.left == other.left:
                    left_open = self.left_open and other.left_open
                    new_item = Item(
                        left_open=left_open,
                        right_open=self.right_open,
                        left=self.left,
                        right=self.right
                    )
                else:
                    left = other.left
                    left_open = other.left_open
                    if not left:
                        left = self.left
                        left_open = self.left_open
                    new_item = Item(
                        left_open=left_open,
                        right_open=self.right_open,
                        left=left,
                        right=self.right
                    )
            elif other_start_is_in_first and other_end_is_in_first and not \
                    first_start_is_in_other and not first_end_is_in_other:
                new_item = copy.deepcopy(other)
            elif other_start_is_in_first and other_end_is_in_first and not \
                    first_start_is_in_other and first_end_is_in_other:
                right_open = other.right_open and self.right_open
                new_item = Item(
                    left_open=other.left_open,
                    right_open=right_open,
                    left=other.left,
                    right=other.right
                )
            elif other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and not first_end_is_in_other:
                if first_line.start == other_line.start:
                    left_open = self.left_open and other.left_open
                    new_item = Item(
                        left_open=left_open,
                        right_open=other.right_open,
                        left=other.left,
                        right=other.right
                    )
                else:
                    new_item = Item(
                        left_open=self.left_open,
                        right_open=other.right_open,
                        left=self.left,
                        right=other.right
                    )
            elif other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and first_end_is_in_other:
                left_open = self.left_open and other.left_open
                right_open = self.right_open and other.right_open
                new_item = Item(
                    left_open=left_open,
                    right_open=right_open,
                    left=other.right,
                    right=other.right
                )
            elif not other_start_is_in_first and other_end_is_in_first and \
                    first_start_is_in_other and not first_end_is_in_other:
                if first_line.start == other_line.end:
                    new_item = Item(
                        left_open=True,
                        right_open=True,
                        left=other.right,
                        right=other.right
                    )
                else:
                    new_item = Item(
                        left_open=self.left_open,
                        right_open=other.right_open,
                        left=self.left,
                        right=other.right
                    )
            elif other_start_is_in_first and not other_end_is_in_first and not \
                    first_start_is_in_other and first_end_is_in_other:
                if first_line.end == other_line.start:
                    if self.right_open and other.left_open:
                        new_item = Item(
                            left_open=True,
                            right_open=True,
                            left=other.right,
                            right=other.right
                        )
                else:
                    left = other.left
                    left_open = other.left_open
                    if not left:
                        left = self.left
                        left_open = self.left_open
                    new_item = Item(
                        left_open=left_open,
                        right_open=self.right_open,
                        left=left,
                        right=self.right
                    )
        return new_item

    def is_intersect(self, other, is_or=False):
        """
        判断两式是否 相交
        :param other:
        :param is_or:
        :return:
        """
        first_line = Line(start=self.left, end=self.right)
        other_line = Line(start=other.left, end=other.right)
        if (
                first_line.in_line(other_line.start, is_end=False)
                or first_line.in_line(other_line.end)
                or other_line.in_line(first_line.start, is_end=False)
                or other_line.in_line(first_line.end)
        ):
            sort_list = self.sort_match_line(first_line, other_line)
            sort_list = [i if i != "0" else "" for i in sort_list]
            sort_list = [i if i != "99999999" else "" for i in sort_list]
            if len(sort_list) == 4:
                if not is_or:
                    is_left_null = False
                    is_right_null = False
                    if not sort_list[0]:
                        is_left_null = True
                    if not sort_list[-1]:
                        is_right_null = True
                    left_open = self.is_open(other, sort_list[1], is_left=True, is_null=is_left_null)
                    right_open = self.is_open(other, sort_list[2], is_null=is_right_null)
                    return Item(
                        left_open=left_open,
                        right_open=right_open,
                        left=sort_list[1],
                        right=sort_list[2],
                    )
                else:
                    is_left_null = False
                    is_right_null = False
                    if not sort_list[0]:
                        is_left_null = True
                    if not sort_list[-1]:
                        is_right_null = False
                    left_open = self.is_open(other, sort_list[0], is_left=True, is_or=True, is_null=is_left_null)
                    right_open = self.is_open(other, sort_list[-1], is_or=True, is_null=is_right_null)
                    sort_flag, sort_is_compare = self.to_compare(sort_list[1], sort_list[2])
                    if sort_is_compare and sort_flag == 0:
                        if sort_list[2] == self.right:
                            if self.right_open or other.left_open:
                                return Item(
                                    left_open=self.left_open,
                                    right_open=other.right_open,
                                    left=sort_list[0],
                                    right=sort_list[-1],
                                )
                            else:
                                return ItemGroup(self, other, is_or=True)
                        elif sort_list[2] == self.left:
                            if self.left_open or other.left_open:
                                return Item(
                                    left_open=left_open,
                                    right_open=right_open,
                                    left=sort_list[0],
                                    right=sort_list[-1],
                                )
                            else:
                                return ItemGroup(self, other, is_or=True)
                        else:
                            return Item(
                                left_open=left_open,
                                right_open=right_open,
                                left=sort_list[0],
                                right=sort_list[-1],
                            )
                    elif sort_is_compare and sort_flag < 1:
                        if self.right == sort_list[1]:
                            return ItemGroup(self, other, is_or=True)
                        else:
                            return Item(
                                left_open=left_open,
                                right_open=right_open,
                                left=sort_list[0],
                                right=sort_list[-1]
                            )
                    else:
                        raise ValueError(f"{sort_list[1]}, {sort_list[2]}不可比较")
            else:
                return Item(valid=False)
        else:
            if is_or:
                items = [self, other]
                return ItemGroup(*items, is_or=True)
            else:
                return Item(valid=False)

    def merge(self):
        return self

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def to_compare(self, one_version, two_version):
        from version import get_base_version
        flag = 1
        is_compare = True
        try:
            one_version_obj = get_base_version(package_type="snyk", version_name=one_version)
            two_version_obj = get_base_version(package_type="snyk", version_name=two_version)
            flag = one_version_obj.__cmp__(two_version_obj)
        except Exception:
            is_compare = False
        return flag, is_compare

    def __cmp__(self, other, is_or=True):
        flag = 1
        first_line = Line(start=self.left, end=self.right)
        other_line = Line(start=other.left, end=other.right)
        if (
                first_line.in_line(other_line.start, is_end=False)
                or first_line.in_line(other_line.end)
                or other_line.in_line(first_line.start, is_end=False)
                or other_line.in_line(first_line.end)
        ):
            s_left = self.left if self.left else "0"
            o_left = other.left if other.left else "0"
            left_flag, left_is_compare = self.to_compare(s_left, o_left)
            s_right = self.right if self.right else "99999999999"
            o_right = other.right if other.right else "99999999999"
            right_flag, right_is_compare = self.to_compare(s_right, o_right)
            if left_is_compare and right_is_compare:
                if left_flag == 0 and right_flag == 0:
                    flag = 0
                elif (left_flag == 0 and right_flag == -1) or left_flag == -1:
                    flag = -1
            # else:
            #     flag = -1
        else:
            s_right = self.right if self.right else "99999999999"
            o_left = other.left if other.left else "0"
            left_flag, left_is_compare = self.to_compare(s_right, o_left)
            if left_is_compare:
                if left_flag == 0 or left_flag == -1:
                    flag = -1
                elif left_flag == 1:
                    flag = 1
            # else:
            #     flag = -1
        return flag


class ItemGroup(ItemBase):
    def __init__(self, *items, is_or=True):
        self.items = list(items)
        self.is_or = is_or

    @property
    def all_equal(self):
        all_equal, _ = self._get_all_or()
        return all_equal

    @property
    def all_other(self):
        _, all_other = self._get_all_or()
        return all_other

    def _get_all_or(self):
        if not hasattr(self, '__get_all_or__'):
            all_equal = set()
            all_other = []
            for item in self.items:
                if isinstance(item, Item):
                    if self.is_or and item.left == item.right and item.left and item.right:
                        all_equal.add(item.left)
                    else:
                        all_other.append(item)
                elif isinstance(item, ItemGroup):
                    all_equal = all_equal | item.all_equal
                    all_other += item.all_other
            setattr(self, '__get_all_or__', (all_equal, all_other))
        return getattr(self, '__get_all_or__')

    def __str__(self):
        return self.get_value()

    def clone(self):
        self.items = copy.deepcopy(self.items)
        return ItemGroup(*self.items, is_or=self.is_or)

    def merge_and(self, other):
        """
        a & (c | d)
        (a & c) | (a & d)
        """
        assert self.is_or
        if isinstance(other, ItemGroup):
            assert other.is_or
        sub_items = [ItemGroup(item, other, is_or=False) for item in self.items]
        ret = ItemGroup(*sub_items, is_or=True)
        return ret.merge()

    def merge_or(self, other):
        is_in = False
        if isinstance(other, Item):
            for i in self.items:
                part_i = other.is_intersect(i, is_or=True)
                if isinstance(part_i, Item) and part_i.valid:
                    is_in = True
                    self.items.remove(i)
                    self.items.append(part_i)
                    break
                if other.get_value() == i.get_value():
                    is_in = True
                    break
            if not is_in:
                self.items.append(other)
        else:
            for other_i in other.items:
                part_i = other_i.is_intersect(self, is_or=True)
                if isinstance(part_i, Item):
                    continue
                else:
                    self.items.append(other_i)
        return ItemGroup(*self.items, is_or=True)
        # return ItemGroup(*self.items, *(other.items if isinstance(other, ItemGroup) else [other]), is_or=self.is_or)

    def merge(self):
        ret = None
        for item in self.items:
            if isinstance(item, ItemGroup):
                item = item.merge()
            if ret is None:
                try:
                    if item.is_valid():
                        ret = item
                    elif not self.is_or:
                        return Item(valid=False)
                except Exception:
                    ret = item
            elif self.is_or:
                if item.is_valid():
                    ret = ret.merge_or(item)
            else:
                if not item.is_valid():
                    return Item(valid=False)
                ret = ret.merge_and(item)
                if not ret.is_valid():
                    return Item(valid=False)
        return ret.merge_finish() if isinstance(ret, ItemGroup) else ret

    def merge_finish(self):
        assert self.is_or
        from version import get_base_version, version_compare
        for item in self.items:
            assert isinstance(item, Item)
        new_items = sorted(self.items)
        ret = []
        last = new_items[0]
        for i in range(1, len(new_items)):
            right = last.right
            left = new_items[i].left
            if not right:
                right = "99999999"
            if not left:
                left = '0'
            flag = version_compare("snyk", right, left)
            # flag = get_base_version(version_name=right, package_type="snyk").__cmp__(left)
            if flag == 1:
                final_right = new_items[i].right
                if not final_right:
                    final_right = "99999999"
                right_flag = get_base_version(version_name=right, package_type="snyk").__cmp__(final_right)
                if right_flag == 1:
                    last = Item(left=last.left, right=last.right, left_open=last.left_open, right_open=last.right_open)
                elif right_flag == 0:
                    if new_items[i].right_open or last.right_open:
                        last = Item(left=last.left, right=last.right, left_open=last.left_open, right_open=True)
                    else:
                        last = Item(left=last.left, right=last.right, left_open=last.left_open, right_open=False)
                else:
                    last = Item(left=last.left, right=new_items[i].right, left_open=last.left_open,
                                right_open=new_items[i].right_open)
            elif flag == 0:
                if new_items[i].left_open or last.right_open:
                    last = Item(left=last.left, right=new_items[i].right, left_open=last.left_open,
                                right_open=True)
                else:
                    ret.append(last)
                    last = new_items[i]
            else:
                ret.append(last)
                last = new_items[i]
        ret.append(last)
        while len(ret) > 1 and ret[0].get_value() == '-':
            ret.pop(0)
        if len(ret) == 1:
            return ret[0]
        else:
            return ItemGroup(*ret, is_or=True)

    def get_value(self):
        assert self.is_or
        version = ""
        for item in self.items:
            if str(item):
                if str(item) != str(self.items[-1]):
                    version = version + str(item) + "||"
                else:
                    version = version + str(item)
        # return f"{'||'.join([str(item) for item in self.items if item.is_valid()])}"
        return version
