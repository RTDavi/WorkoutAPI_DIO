run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@Path=$Path:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@Path=$Path:$(pwd) alembic upgrade head
	