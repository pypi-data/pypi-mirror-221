import uuid
from faker import Faker
from pydantic import BaseModel, field_validator


fake = Faker()
Faker.seed(1)


class Weight(BaseModel):
    mass_kg: float
    last_measured: str


class Feeding(BaseModel):
    amount_kg: float
    cron_schedule: str
    last_measured: str


class MilkProduction(BaseModel):
    last_milk: str
    cron_schedule: str
    amount_l: float


class Cow(BaseModel):
    id: str
    name: str
    sex: str
    birthdate: str
    condition: str
    weight: Weight
    feeding: Feeding
    milk_production: MilkProduction
    has_calves: bool

    @field_validator("sex")
    def sex_must_be_valid(cls, sex):
        valid_sexes = ["Male", "Female"]
        if sex not in valid_sexes:
            raise ValueError('Sex must be either "Male" or "Female".')
        return sex

    @classmethod
    def generate_fake(cls):
        return cls(
            id=str(uuid.uuid4()),
            name=fake.first_name(),
            sex=fake.random_element(elements=["Male", "Female"]),
            birthdate=str(fake.date_time()),
            condition=fake.random_element(elements=["Healthy", "Sick"]),
            weight=Weight(
                mass_kg=fake.random_int(min=1000, max=1500),
                last_measured=str(fake.date_time()),
            ),
            feeding=Feeding(
                amount_kg=fake.random_int(min=1, max=10),
                cron_schedule="0 */6 * * *",
                last_measured=str(fake.date_time()),
            ),
            milk_production=MilkProduction(
                last_milk=str(fake.date_time()),
                cron_schedule="0 8,12,16,20 * * *",
                amount_l=fake.random_int(min=1, max=10),
            ),
            has_calves=fake.random_element(elements=[True, False]),
        )
