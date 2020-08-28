<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# Sweet Eats Bakery Online Shop
# Code Institute - Full Stack Frameworks with Django Milestone Project (4)

This is an online shop for Sweet Eats Bakery. 

To meet the increasing demand of consumers turning to online platforms for food products like cakes, chocolates and macarons, Sweet Eats requires a platform to increase revenue by selling high their products online. Moreover, it gives a platform for consumers to leave their reviews and recommend other users visiting the site.

Hence, an online mobile-friendly website was created to enable potential consumers to register for an account, login, browse through the shop items, view details of the item, add or remove products from their shopping cart, checkout, make payments for their purchase and even leave reviews for the items.

For the site owner, there will be an admin panel where they are able to search for the existing items, create new item listing, edit existing listing and remove items that are not for sale at the shop.

The website may be accessed from [here](https://dlcw-sweeeat.herokuapp.com/)

##### To login as a site user
`username: chocolate`

`password: cakeslover`

##### To login as a site admin

`username: adminuser`

`password: adminaccess123`

## UX

In order to achieve the intent of capturing the viewers attention to the products that are showcased, the website aims to portray a very simple and minimalist feel. The use of blank space and clean minimalist icons allow the viewer attention to be focused mainly on the products. A five-colour palette scheme consisting of mostly warm colours was maintained throughout the whole website design. This is consistent and evident through the the wireframe. A copy of the wireframe me be viewed [here](https://drive.google.com/file/d/1DaxBSyrRYWKR2WWXav0VTNfP4I0tSy30/view?usp=sharing).

Besides the look, the website also ensure that it is user-friendly and interactive. When a user first enter the website, they will be greeted by four  photos (shows description upon hovering) which illustrate the categories of the items followed by a main navigation button which clearly specifies the intent - to bring them to view the products.

The use of minimal clicks to navigate the website allow users to have a good browsing experience when going through the website. Icons were placed with thought to allow users to intuitively click on them to navigate pages. 

At the products page, users are able to easily search the items by the name, category and/or the price. When the viewers click view more, they will be brought to show description, price and add to cart feature of the product.
A review section was added to allow some degree of interaction among the customers. They may add, edit or event delete review entries uploaded. 

When a user perform an action, a notification will pop-up which informs the user that the action is completed successfully or is an unsuccessful attempted.

When a site user or an admin user logins to the site, the top nav-bar shows different navlinks for different users. For instance, for a site user, it will just show welcome (username) in the middle section and a logout button at the far right. For a site admin, it will show welcome (admin name) in the middle section and a logout and admin button at the far right. The admin button brings the admin user to the admin site to view, add, update and delete products.

A user will be highly encouraged to register an account to view more features such as making a purchase and leaving a review. Hence, there will be a message to direct them to the register or login page.

Apart from that, the display of the website differs for a desktop and mobile view to allow the same experience on all devices and platforms. All in all, the website is created with the intent to fulfil the users' needs in a straighforward and forthcoming approach.

## User Stories
![userstories](readme/userstories.jpg)

## Features
 
### Existing Features
1. Landing Page, Our Story, Contact Us and Overall (Navigation Bar and Footer)
* Landing Page
    - The site user will be welcomed with four nice photos which illustrates the categories of items the shop sells. Upon hovering on each image, there will be a short description on the category.
    - The site user can also quickly access the Shop by clicking the center aligned button "Shop Now". To maitain the overall thematic deisgn, upon hovering on the button, it will change to a pink button.
* Our Story
    - Shows the story of the company in bootstrap card format.
    - Clean and consistent with overall theme
* Contact Us
    - Shows the contact us of the company in bootstrap card format.
    - Clean and consistent with overall theme
    - Button with mailto: the company email
* Navigation Bar (Mobile Responsive)
    -   The navigation bar collapse in mobile view and will be able to toggle open and close the navgation bar by tapping on the burger icon.
    - Sticky-top Navigation bar ensures easy navigation for the site users.
    - The top tier navgiation bar has three sections (Left, Middle and Right)
        - Left: Logo for the company prominently sits on the top left of the page
        - Middle: This shows a welcome message to the login user "Welcome, 'username'"
        - Right: The navigation links changes with the log in user. If the login user is a customer, it will just show logout. If the login user is an admin user, it will show logout and admin. The admin will be able to then access the admin page easily to perform (C-Create, R-Read, U-Update, D-Delete) CRUD tasks on the product listings.
* Footer (Mobile Responsive)
    - A fully mobile responsive footer that changes its layout when in mobile-view.
    - A site map which also show links to the various part of the website

2. Admin Page
* When an admin user login to the site, the admin navigation link will appear on the top right of the webpage.
* Upon landing on the admin page, the admin user may:
    - Add New Products 
    - View and search for existing product listings in the database based on name, category and price
    - Edit any existing product listing in the database (Note: There is a cloudinary error for uploading the image at the edit page, will need to upload and submit twice before it can successfuly update)
    - Remove any existing product in the database

3. Register an account and Logins
* Login and logout
* Register an account
* Password register

4. Sweet Selections (Shop)
* View all products in the shop or search them based on name, category and price
* When a site user is not login:
    - View individual product details, price, description and reviews of the product
* When a site user is login:
    - View individual product details, price, description and reviews of the product
    - Add to cart function will be shown
    - Add a review function will be shown 
    - Site user may perform (C-Create, R-Read, U-Update, D-Delete) CRUD tasks to add a review, view the review in the bottom section, edit the review and delete the review. User will only be able to edit and delete reviews added by themself
* When a site admin is login:
    - Add to cart function will be shown
    - Add a review function will be shown
    - Edit button will be shown (Note: There is a cloudinary error for uploading the image at the edit page, will need to upload and submit twice before it can successfuly update)
    - Delete button will be shown to delete the product listing in the database

5. Cart
* Site user will be able to update the quantity of the item added in the cart
* Site user may remove (delete) item that is added to the cart
* Confirming the order will bring the user to the add address section and checkout

6. Checkout
* Site user will be able to add the delivery address
* After adding the delivery address, user will be directed to the payment gateway - Stripe to make payment using any form of credit card

### Features Left to Implement
Due to the project time constraints and longer learning period of Django, features that will better complete a user experience for the online shop were left out
1. Add Pagination to the shop (limiting to 8 items per page)
2. Site User to be able to view their transaction history and delivery status
3. Site User will be able to add a profile page to add in their personal details (delivery address, name, profile picture and edit when they prefer)
3. Discount codes function for product
4. Admin user will be able to change the delivery status of the purchases for each user.

## Technologies Used

### Frameworks
1. Django 2 (2.2.6)
2. Python 3

### Styling
* [HTML](https://www.w3schools.com/html/) - standard markup language for creating web pages
    - HTML is basically used throughout the whole document to construct the various segments and putting things together

* [CSS](https://www.w3schools.com/css/) - describes the style of the HTML document
    - CSS is important to maintain the look, style and feel of the website

* [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - popular framework for building responsive, mobile-first sites
    - Bootstrap framework makes things easier to have basic features and minimised the use of css styling with bootstrap features

* [Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Display Django forms nicely on the webpages

* [Javascript](https://www.youtube.com/watch?v=gnDOjWUSHks)
    - Javascript is used to enhance the Cloudinary upload photo experience

* [Google Fonts](https://fonts.google.com/)
    - Used of appropriate fonts for website theme

* [Font Awesome](https://fontawesome.com/)
    - Add icons to enhance the feel for clickable links

### Additional Plugins
* Stripe (payments)
* Cloudinary (uploading of photos)
* Gunicorn (WSGI application server)
* Psycopg2 (PostgreSQL database adaptor for Python)
* Pillow (PIL fork)
* Whitenoise (simplified static file serving for Python web apps)

### Database
* PostgreSQL
* dbsqlite3

## Testing
The site is manually tested on a macbook pro, windows laptop, andriod mobile device (Samsung note 9) and ipad to ensure the responsiveness and that all the links work well.

* Page content fits device width and is responsive on all devices
* Text on the page is readable
* Links and tap targets are sufficiently large and touch-friendly
* The navbar to access all the pages (Login, Register, Logout, Admin, Home, Sweet Selections, Our Story, Contact Us and Shopping Cart) is tested to ensure it works well on all platforms

On all platforms, the following were tested

1. Landing Page
    - The hover effect on the images works well with every refresh
    - The navigation button is able to bring the users to the shop works well
2. Shop (Products)
    - All the item listings show up without error on every refresh
    - Navbar links work well
    - Searchbar: Selected a category and enter a blank search term displays all listings of the category
    - Searchbar: Enter a "search term" displays all listings of the "search term"
    - Searchbar: Enter a "maximum price" displays all listings below the search price
    - Searchbar: Stack the requirements and it displays the listings well
    - Upon click on view more, it was redirected to show the details of the particular item
3. View Individual Product Page
    * Not logged in, logged in as site user, logged in as admin user:
        - Details were displayed well with click from main listing page
    * Login in as site user:
        - Add to cart button works well
        - CRUD works well for adding, view, edit and delete reviews
        - Added a review, edited and deleted it, works well
    * Login in as site admin:
        - Add to cart button works well
        - CRUD works well for adding, view, edit and delete reviews
        - Added a review, edited and deleted it, works well
        - Delete item works well
        - Edit item works well
4. Cart
    - Updated quantity in cart and amount increase accordingly
    - Removed an item in cart
    - Click on button and it works well to bring to the next page to add in delivery details
5. Checkout
    - Form to add in delivery address works well
    - After submission, was directed to the strips payment page
    - Tested with the test credit card number and payment is completed and user redirected back to the product listings page
6. Admin Page
    * Add Product Listing
        - Add product form and works well
    * Edit Product listing Page
        - Details displayed were of selected entry from main products page
        - Tried to update all fields and uploaded a new image and it displays well and return to main products page
        (Note: There is a cloudinary error for uploading the image at the update page, will need to upload and submit twice before it can successfuly update)
    * Delete Product listing Page
        - Details displayed were of selected entry from main products page
        - Click on Delete and Entry was deleted and return to main admin page
        - Click on cancel and entry was not deleted and return to main admin page
7. Login, logout, forget password and register
    - Tested to resgister an account and received email verification
    - Verified user and login and it works
    - Logout and it works


The site was manually tested on different browsers (Chrome, Safari, Morzilla Firefox and Internet Explorer).
The site works well on all browsers.

The site was also tested using online platform [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) and results show that page is mobile friendly and easy to use on a mobile device.


## Deployment
This project is coded on Gitpod and respositories are on GitHub. The website is deployed and hosted using Heroku directly from the master branch in Github. The database was created on Django's sqlite but transferred into Postgres after deployment on Heroku.

From my git repository, I have proceed to deploy to Heroku.
For deployment to Heroku, the following steps were taken
1. Install Dependencies
```
pip3 install gunicorn
pip3 install psycopg2
pip3 install Pillow
pip3 install whitenoise 
pip3 install dj_database_url
```
2. Add Whitenoise to the Middleware inside my project folder - settings.py
```
MIDDLEWARE = [
.....
'whitenoise.middleware.WhiteNoiseMiddleware'
]
```
3. Ensure my .gitignore file is created in the root folder
4. Login to Heroku on the gitpod terminal
```
heroku login -i
```
5. Create the Heroku App via the Gitpod terminal
```
heroku create dlcw-sweeeat
```
6. Double check the Heroku App has been created successfully.
Heroku will add two origins to your git remotes. Do a check by running the following:
```
git remote -v
```
7. Copy environment variables over from .env to Heroku Dashboad >> Settings >> Reval Config Vars
8. In the root folder, create a file named Procfile
9. Open the Procfile, and enter the following 
```
web: gunicorn SweeEatProject.wsgi:application
```
10. Update ALLOWED_HOSTS inside Project folder > settings.py
```
https://dlcw-sweeeat.herokuapp.com/
```
11. Generate requirements.txt so that Heroku will know what packages install.
```
pip3 freeze --local > requirements.txt
```
12. Add STATIC_ROOT to your settings.py file
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
13. Before deploying to Heroku,  commit the code to your git repository
```
git add .
git commit -m "your commit message"
git push
```
14. Finally, make a push to Heroku
```
git push heroku master
```

## Credits

### Content
- The text for the Category Description is taken and modified from the following website
    - Cupcakes Description - [Twelve Cupcakes](https://twelvecupcakes.com/menu/cupcakes/)
    - Chocolate Truffles - [Awfully Chocolate](https://www.awfullychocolate.com/the-perfect-gift/gorgeous-truffles/)
    - Macarons - [TWG](https://twgtea.com/tea-table/gourmet-delicacies/twg-tea-macarons-assorted)
    - Whole Cakes - [Awfully Chocolate](https://www.awfullychocolate.com/chocolate-cakes/signature-cakes/)

- The quote and text for the "Our Story" is taken and modified from the following website
    - [Edith Patisserie](https://www.edithpatisserie.com/about-us)
    - [Pinterest] (https://www.pinterest.com/pin/538602436666824480/?nic_v2=1av5yJr3C)



### Media
- The photos used in this site were all obtained from [Unsplash](https://unsplash.com/) - a stock image library.
    Please refer to the Links of images used
    - https://unsplash.com/photos/li0iC0rjvvg
    - https://unsplash.com/photos/2XK4UufbjdU
    - https://unsplash.com/photos/_TN1m5R1pFI
    - https://unsplash.com/photos/dcPNZeSY3yk
    - https://unsplash.com/photos/GTMGG-xvxdU
    - https://unsplash.com/photos/On2VseHUDXw
    - https://unsplash.com/photos/tA3sJ4u09eU
    - https://unsplash.com/photos/9sKcBBMII6Q
    - https://unsplash.com/photos/a0ex7idMUG4
    - https://unsplash.com/photos/hB6HN7hzcgg
    - https://unsplash.com/photos/j_bB5QqigfU
    - https://unsplash.com/photos/116JtRtf0QI
    - https://unsplash.com/photos/xatIo9Ksfb0
    - https://unsplash.com/photos/Uv5FRPKBwvU
    - https://unsplash.com/photos/KPpU6rCIziQ
    - https://unsplash.com/photos/UxnSB5nTZDs
    - https://unsplash.com/photos/mLfDsNR-bs0
    - https://unsplash.com/photos/8Vuq1nSzmgo
    - https://unsplash.com/photos/yHpA0SYKfMY
    - https://unsplash.com/photos/rXB9YjOQX8I
    - https://unsplash.com/photos/lo0eEGA2fYk
    - https://unsplash.com/photos/On2VseHUDXw
    - https://unsplash.com/photos/P68yv6bC2pI
    - https://unsplash.com/photos/ySxSlqeC0YM
    - https://unsplash.com/photos/OYKZNEwdZus

### Acknowledgements
- CSS Styling by [Bootstrap4](https://getbootstrap.com/)
- All fonts used for this site are obtained from [google fonts](https://fonts.google.com/)
- All icons used for this site are obtained from [Fonts Awesome](https://fontawesome.com/)
- Theme and Design of Website is inspired by [Swee tooth](https://sweettooth.qodeinteractive.com/landing-page/?utm_source=pinterest&utm_medium=pin&utm_campaign=bestwpdesign) and [Edith Patisserie](https://www.edithpatisserie.com/about-us)
- Image Hover Effects is modified from [Mike Tricking](https://miketricking.github.io/bootstrap-image-hover/)
- Footer is modified from [Color Lib](https://colorlib.com/wp/bootstrap-footer/)
- Icons, design and wireframe are created using [Apple Keynote](https://www.apple.com/sg/keynote/)
- Django is learnt and taught from walkthrough by Instructor, Paul Chor from [Trent Global College](https://www.trentglobal.edu.sg/)

## This website created is for educational use.
## NOTE: This online shop is entirely fictional 

