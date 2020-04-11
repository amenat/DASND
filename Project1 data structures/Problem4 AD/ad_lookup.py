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
    ''' Return True if user is in the group, False otherwise.'''

    #check inputs
    if not isinstance(user, str): raise ValueError('User must be a string')
    if not isinstance(group, Group): raise ValueError('group must be instance of `Group`')

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
sub_child_2.add_user('DeepBlue')

child2.add_group(sub_child_2)
parent.add_group(child2)

print(is_user_in_group('sub_child_user', parent))    # True - sub_child_exist in parent
print(is_user_in_group('DeepBlue', child))           # False - Deepblue exist in another subtree
print(is_user_in_group('sub_child_user', child2))    # False - sub_child_user exists in another subtree
print(is_user_in_group('DeepBlue', parent))          # True - DeepBlue is present in parent tree
print(is_user_in_group('DeepBlue', child2))          # True - DeepBlue is present in child2 subtree
print(is_user_in_group('mcboatface', ['mcboatface', 'boaty'])) # Raise value error as input group is a list not Group
