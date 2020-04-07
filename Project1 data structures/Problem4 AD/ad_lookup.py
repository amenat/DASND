from typing import List


'''In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids. '''
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    ''' Return True if user is in the group, False otherwise.

    Runtime complexity: O(sum(len(group) for group in all_groups_recursively))
    Or in asymptotic terms O(len(groups) * len(all_users))

    it's difficult to write sigma notation here.
    Assuming users can be part of multiple groups in Active directory and there's no restriction on group and user count in group.
    This implies that we will have to check each and every group/subgroup recursively and if user can be part of any and all groups.

    *If users are unique a particular group* then this reduces to near linear time: O(len(groups) + len(all_users))
    Since Class Group doesn't ensure uniqueness of users in anyway, I've assumed that users can be duplicated across groups.

    '''
    # search in users of current group
    if user in group.get_users():
        return True
    # if there are no subgroup user doesn't exits in AD tree
    elif len(group.get_groups()) == 0:
        return False
    # else if subgroups exist recurse and find if any of them have the user
    else:
        # python does lazy evaluation on `any` so this is equal to writing a for loop -
        # https://docs.python.org/3/library/functions.html#any
        return any(is_user_in_group(user, sub_grp) for sub_grp in group.get_groups())



# test cases
parent = Group('parent')
child = Group('child')
sub_child = Group('subchild')

sub_child_user = 'sub_child_user'
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

child2 = Group('younger child')
sub_child_2 = Group('Subchild 2')
sub_child_2.add_user('Ankush')

child2.add_group(sub_child_2)
parent.add_group(child2)

assert is_user_in_group('sub_child_user', parent) == True
assert is_user_in_group('Ankush', child) == False
assert is_user_in_group('sub_child_user', child2) == False
assert is_user_in_group('Ankush', parent) == True
assert is_user_in_group('Ankush', child2) == True
