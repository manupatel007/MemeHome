from faker import Faker
from models import Tasks, User1

faker = Faker()
user = User1.objects.all()[0]
for i in range(100):
    name = faker.name()
    title = faker.text(max_nb_chars=12)
    description = faker.text()
    v = Tasks(uid=user, task_title=v.task_title, task_description = v.task_description)
    v.save()
