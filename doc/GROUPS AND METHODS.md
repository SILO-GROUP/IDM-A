# Access Control Specifications

There are groups built in to IDM/A which are associated with the methods provided by the API.  

## A Deny-First Model

In terms of development philosophy, IDM/A uses a "deny first" approach:

Actions are denied unless an explicit exception is made in the API code.  For instance, all methods initially require an authenticated session at the very least, yet, the creation of an account for a web application should not require an authenticated session, so, that method is explicitly excepted from this requirement in the code for the API.  This allows defects to be a product of action on the developer's part as opposed to gaps in visibility.  (*Note: public creation of user accounts can be disabled depending on use case.)

## Wheel is King

Methods on users, groups and sessions, while restricted to built-in groups, are universally allowed only to members of the group named "wheel".

## RAILS ON CRUD

No, we're not using Ruby on Rails to blockchain your NFT to the kubernetes when we say "CRUD ON RAILS".  What this phrase means is that IDM/A is essentially a CRUD app for users, groups, and sessions.  The access control mechanisms are just a layer of rails on top of that to secure the use of those CRUD features.

## Groups and Methods

### Methods
A method is a URL on the IDM/A endpoint that peforms an action on users, groups, and sessions.

### Groups
A group is an object associated with 0 or more users.

## Surfaces
```
IDM/A
├── authenticated_users
│   └── activated_users
│       ├── member_of_a_group
│       │   ├── consumer_system_actions
│       │   ├── restricted_idma_actions
│       │   └── unrestricted_idma_actions
│       └── not_a_member_of_a_group
│           ├── consumer_system_actions
│           └── unrestricted_idma_actions
├── deactivated_users
└── unauthenticated_users
    └── (create_user)
```

- `authenticated users` have a session. 
- `unauthenticated users` do not have a session.
- `activated users` have their "active" attribute set to `True`.  They are granted a session after authentication.
- `deactivated users` have their "active" attribute set to `False`.  They are not granted a session even if they pass authentication.  These users can do nothing.
- `authenticated users` who are `activated users` and are a `member_of_a_group` may execute IDM/A methods associated with any of the groups they are a member of, in addition to actions controlled by the consumer system of IDM/A.  The consumer system may also use group membership to restrict or allow actions based on membership groups specific to that consuming system.
- `authenticated users` who are `activated users` and are `not_a_member_of_a_group`, beyond self-management actions such as updating password, are constrained entirely to actions in the consuming system of IDM/A that do not require group membership and are specific to that consuming system.

### Group/Method Associations
*These are incomplete.

| GROUP             | Provides                                                               |
|-------------------|------------------------------------------------------------------------|
| wheel             | Unrestricted access to all authenticated and group-restricted actions. |
| sys-create_users  | Optionally required for creating users.                                |
| sys-list_users    | List all users and their associated groups.                            |
| sys-modify_users  | Modify user attributes.                                                |
| sys-list_groups   | List all groups and their associated members.                          |
| sys-modify_groups | Modify group attributes, including membership.                         |
| sys-list_sessions | List all sessions and their associated users.                          |
