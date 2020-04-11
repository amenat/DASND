To check if a user exists in any group I first...

    1. Check if user exists in current group
    2. if current groups has subgroups (this is basecase for recursion)
       1. check if user exists in any of the subgroups recursively


Runtime complexity:

O(sum(len(group) for group in all_groups_recursively))

Or in asymptotic terms O(len(groups) * len(all_users))

Assuming users can be part of multiple groups in Active directory and there's no restriction on group and user count in group.
This implies that we will have to check each and every group/subgroup recursively and if user can be part of any and all groups.

*If users are unique a particular group* then this reduces to near linear time: O(len(groups) + len(all_users))
Since Class Group doesn't ensure uniqueness of users in anyway, I've assumed that users can be duplicated across groups.

Space complexity is O(1) as no space is being used. This doesn't include call stack. Since python doesn't have tail recursion; the call stack will grow O(len(all group))  in worst case.