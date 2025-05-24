gh issue create --title "Set up Django project with apps: posts, photos, comments" --body "As a developer, I want to set up the base Django project with three apps so that each app can handle its own logic.

### Acceptance Criteria
- Apps created and registered in settings.py
- Base urls configured
- Models initialized in each app

### Tasks
- [ ] Create Django project
- [ ] Create apps: posts, photos, comments
- [ ] Register apps
- [ ] Setup base URLs" --repo JNicolin/MS3-ReedmakerStudio

gh issue create --title "Implement CRUD for Post model" --body "As a user, I want to create, read, update, and delete posts so that I can manage my blog content.

### Acceptance Criteria
- CRUD views work for authenticated users
- Post list and detail pages load
- Only authors can edit/delete

### Tasks
- [ ] Create Post model
- [ ] Add PostForm
- [ ] Implement list, detail, create, update, delete views" --repo JNicolin/MS3-ReedmakerStudio

gh issue create --title "Implement CRUD for Comment model" --body "As a user, I want to comment on content so I can participate in discussion.

### Acceptance Criteria
- Comments visible on detail pages
- Only authors can edit/delete
- Comment form displays properly

### Tasks
- [ ] Create Comment model
- [ ] Add generic relation to content
- [ ] Implement views and form" --repo JNicolin/MS3-ReedmakerStudio

gh issue create --title "Connect Comment model generically to both Post and Reed" --body "As a developer, I want comments to be reusable across content types so I can use one model for multiple apps.

### Acceptance Criteria
- Comments show on both Posts and Reeds
- GenericForeignKey used correctly
- Forms and templates updated

### Tasks
- [ ] Use contenttypes framework
- [ ] Update views to handle related comments
- [ ] Ensure templates render comments" --repo JNicolin/MS3-ReedmakerStudio

gh issue create --title "Design base.html with Bootstrap 5 layout" --body "As a user, I want a consistent layout across pages so I can navigate easily.

### Acceptance Criteria
- Base template includes navbar and footer
- Block structure used for title and content
- Bootstrap CSS linked

### Tasks
- [ ] Create base.html
- [ ] Include navbar and footer
- [ ] Add {% block %} tags" --repo JNicolin/MS3-ReedmakerStudio