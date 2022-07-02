# Access Control Specifications

There are groups built in to IDM/A which are associated with the methods provided by the API.  

## A Deny-First Model

In terms of development philosophy, IDM/A uses a "deny first" approach:

Actions are denied unless an explicit exception is made in the API code.  For instance, all methods initially require an authenticated session at the very least, yet, the creation of an account for a web application should not require an authenticated session, so, that method is explicitly excepted from this requirement in the code for the API.  This allows defects to be a product of action on the developer's part as opposed to gaps in visibility.  (*Note: public creation of user accounts can be disabled depending on use case.)

## Wheel is King

Methods on users, groups and sessions, while restricted to built-in groups, are universally allowed only to members of the group named "wheel".

## RAILS ON CRUD

No, we're not using Ruby on Rails to blockchain your NFT to the kubernetes when we say "RAILS ON CRUD".  What this phrase means is that IDM/A is essentially a CRUD app for users, groups, and sessions.  The access control mechanisms are just a layer of rails on top of that to secure the use of those CRUD features.


## Module Structure
Modules are divided up into a few different common files, with exception to the core module (Pantheon) which mainly contains shared resources and one-offs important to the transparent middleware.

### API.py
This contains route and method declarations for the endpoint.  This is the user-facing code.

### APIModels.py
This is where schemas or models for user input expected in methods declared in API.py are stored.

### Controller.py
Controller code goes here.  This is the layer that interacts with the database and performs any additional logic necessary for feature implementation.  It is important that logic go here so that CLI utilities can consume the controller without re-implementing security logic.

### DatabaseModels.py
ORM models go here.  These are objects that represent table structure in the database.

### Decorators.py
Various decorators are used to create security rules around various methods, usually specific to the module.

### ViewSchemas.py
These are output schemas specifically for output sent to the user.  Output must fit into these schemas to be sent.  

This is a rather important piece as it prevents data you would not want to show to the user (unless you explicitly define it to be visible).

## Groups and Methods

### Methods
A method is a URL on the IDM/A endpoint that performs an action on users, groups, and sessions.

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
- `authenticated users` who are `activated users` and are a `member_of_a_group` may execute IDM/A methods associated with any of the groups they are a member of, in addition to actions controlled by the consumer system of IDM/A.  The consumer system may also use group membership to restrict or allow actions based on membership groups as determined by that consuming system.
- `authenticated users` who are `activated users` and are `not_a_member_of_a_group`, beyond self-management actions such as updating password, are constrained entirely to actions in the consuming system of IDM/A that do not require group membership as determined by that consuming system.

### Group/Method Associations
*These are incomplete.

| GROUP                 | Provides                                                                                                                                     |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| wheel                 | Unrestricted access to all authenticated and group-restricted actions.                                                                       |
| sys-create_users      | Optionally required for creating users.                                                                                                      |
| sys-list_all_users    | List all users and their associated groups.                                                                                                  |
| sys-modify_all_users  | Modify user attributes.  Does not apply to group membership.  Adding a user to or from a group is an operation on that group, not that user. |
| sys-list_all_groups   | List all groups and their associated members. Should be restricted to admins.                                                                |
| sys-modify_all_groups | Modify group attributes, including membership.                                                                                               |
| sys-list_all_sessions | List all sessions and their associated users.  Should be restricted to admins.                                                               |
 | 