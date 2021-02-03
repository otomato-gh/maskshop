# maskshop
Shop corona masks

Exercise:
- Please add a docker-compose file
- Application components:

| Name  | Image                           | Port |
|-------|---------------------------------|------|
| mongo | mongo                           | 2717 |
| api   | otomato/maskshop-api:latest     | 80   |
| front | otomato/maskshop-front:latest   | 80   |

- Run the composition, connect to `front` web page, verify you can add your own mask

- Check the application logs

Now build your own images
Push them to Docker Hub
Change the composition to use your images.
Rerun the composition, verify it still works.
