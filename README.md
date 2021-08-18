# maskshop
Shop corona masks

Exercise:
- Please create a `Dockerfile` for `api` based on instructions in [README](api/README.md)
- Please create a `Dockerfile` for `front` based on instructions in [README](front/README.md)
- Please add a docker-compose file
- Application components:

| Name  | Image                           | Port |
|-------|---------------------------------|------|
| mongo | mongo                           | 2717 |
| api   | build from Dockerfile in `api`  | 80   |
| front | build from Dockerfile in `front`| 80   |

- Run the composition, connect to `front` web page, verify you can add your own mask

- Check the application logs

- Now build and push api and front images to your DockerHub

- Change the composition to use your DockerHub images.

- Rerun the composition, verify it still works.

## Bonus Points
Create another compose file: **docker-compose-dev.yml**
- Use **python:alpine** image for **api** and **front**
- Mount the python code from your workspace with [volumes](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes)
- Run `pip install -r requirements.txt && python api.py` as the command by using [command](https://docs.docker.com/compose/compose-file/compose-file-v3/#command)
