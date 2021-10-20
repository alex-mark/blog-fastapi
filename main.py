from fastapi import FastAPI


app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} from the db"}


@app.get("/blog/unpublished")
def unpublished():
    # fetch blog with id
    return {"data": "All unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id
    return {"data": id}


@app.get("/blog/{id}/comments")
def about(id: int, limit=10):
    # fetch blog with id
    return {"data": {"comments": ["Comment 1", "Comment 2", "Comment 3"]}}


@app.post('/blog')
def create_blog():
    return {"data": "blog has been created."}