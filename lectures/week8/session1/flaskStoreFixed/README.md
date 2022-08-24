# Flask Store Broken Version

## Clone the code and run the app
- Forward Engineer the ERD
- Use the app 1st then look at the code to find the errors
- There are 12 Errors (injected errors)


# Errors by Type

## ERD Errors:
- ORDERED table misspelled
- NN was checked for user.updatedAt
- user.updatedAt didn't have defaults
- product.id didn't have AI checked
- user.updatedAt was actually updatedAT


## SQL Errors:
- product.save() had : not ; for query


## Route Errors:
- Session not pushed to html or called on html for user dash
- order route no post
- Delete route had 'id': id not 'id': product_id

## HTML Errors:
- who ordered should have been item.who.firstName

## Rendering/Visual Errors:
- Dash not showing who created item
- All users could edit.  needed to add user.id to if condition

