from django.test import TestCase

from . import models


class ModelTests(TestCase):

    def test_marital_status_str(self):
        marital_status = models.MaritalStatus.objects.create(
            name="Never Married"
        )

        self.assertEqual(str(marital_status), marital_status.name)

    def test_language_str(self):
        language = models.Language.objects.create(
            name="Malayalam"
        )

        self.assertEqual(str(language), language.name)

    def test_physical_status_str(self):
        physical_status = models.PhysicalStatus.objects.create(
            name="Normal"
        )

        self.assertEqual(str(physical_status), physical_status.name)

    def test_body_type_str(self):
        body_type = models.BodyType.objects.create(
            name="Slim"
        )

        self.assertEqual(str(body_type), body_type.name)

    def test_complexion_str(self):
        complexion = models.Complexion.objects.create(
            name="Fair"
        )

        self.assertEqual(str(complexion), complexion.name)

    def test_created_by_str(self):
        created_by = models.CreatedBy.objects.create(
            name="Self"
        )

        self.assertEqual(str(created_by), created_by.name)

    def test_eating_habit_str(self):
        eating_habit = models.EatingHabit.objects.create(
            name="Vegetarian"
        )

        self.assertEqual(str(eating_habit), eating_habit.name)

    def test_drinking_habit_str(self):
        drinking_habit = models.DrinkingHabit.objects.create(
            name="Non Drinker"
        )

        self.assertEqual(str(drinking_habit), drinking_habit.name)

    def test_smoking_habit_str(self):
        smoking_habit = models.SmokingHabit.objects.create(
            name="Non Smoker"
        )

        self.assertEqual(str(smoking_habit), smoking_habit.name)

    def test_religion_str(self):
        religion = models.Religion.objects.create(
            name="Hindu"
        )

        self.assertEqual(str(religion), religion.name)

    def test_caste_str(self):
        religion = models.Religion.objects.create(name='Hindu')

        caste = models.Caste.objects.create(
            religion=religion,
            name="Ezhava"
        )

        self.assertEqual(str(caste), caste.name)

    def test_star_str(self):
        star = models.Star.objects.create(
            name="Aswathi"
        )

        self.assertEqual(str(star), star.name)

    def test_raasi_str(self):
        raasi = models.Raasi.objects.create(
            name="Medam"
        )

        self.assertEqual(str(raasi), raasi.name)

    def test_dosham_str(self):
        dosham = models.Dosham.objects.create(
            name="No"
        )

        self.assertEqual(str(dosham), dosham.name)

    def test_education_str(self):
        education = models.Education.objects.create(
            name="BE"
        )

        self.assertEqual(str(education), education.name)

    def test_occupation_str(self):
        occupation = models.Occupation.objects.create(
            name="Software Professional"
        )

        self.assertEqual(str(occupation), occupation.name)

    def test_employed_in_str(self):
        employed_in = models.EmployedIn.objects.create(
            name="Private"
        )

        self.assertEqual(str(employed_in), employed_in.name)

    def test_currency_type_str(self):
        currency_type = models.CurrencyType.objects.create(
            name="Rs."
        )

        self.assertEqual(str(currency_type), currency_type.name)

    def test_country_str(self):
        country = models.Country.objects.create(
            name="India"
        )

        self.assertEqual(str(country), country.name)

    def test_state_str(self):
        country = models.Country.objects.create(name='India')

        state = models.State.objects.create(
            country=country,
            name="Tamil Nadu"
        )

        self.assertEqual(str(state), state.name)

    def test_city_str(self):
        country = models.Country.objects.create(name='India')

        state = models.State.objects.create(
            country=country,
            name="Tamil Nadu"
        )

        city = models.City.objects.create(
            state=state,
            name="Coimbatore"
        )

        self.assertEqual(str(city), city.name)

    def test_family_value_str(self):
        family_value = models.FamilyValue.objects.create(
            name="Liberal"
        )

        self.assertEqual(str(family_value), family_value.name)

    def test_family_type_str(self):
        family_type = models.FamilyType.objects.create(
            name="Nuclear Family"
        )

        self.assertEqual(str(family_type), family_type.name)

    def test_family_status_str(self):
        family_status = models.FamilyStatus.objects.create(
            name="Middle Class"
        )

        self.assertEqual(str(family_status), family_status.name)

    # def test_profile_str(self):
    #     profile = models.Profile.objects.create(
    #         user=Utilities.sample_user(),
    #         dob='1995-08-11',
    #         about='Software Engineer working in Bangalore',
    #         height=182,
    #         weight=70,
    #         marital_status=models.Profile.MARITAL_STATUS[0],
    #         mother_tounge=models.Profile.LANGUAGES[0],
    #         physical_status=models.Profile.PHYSICAL_STATUS[0],
    #         profile_created_by=models.Profile.PROFILE_CREATED_BY[0],
    #         eating_habit=models.Profile.EATING_HAIBTS[0],
    #         drinking_habits=models.Profile.DRINKING_HABITS[0],
    #         smoking_habits=models.Profile.SMOKING_HABITS[0],
    #         education=models.Profile.RELIGION[0],
    #         education_institution=models.Profile.RELIGION[0],
    #         occupation=models.Profile.RELIGION[0],
    #         organization=models.Profile.RELIGION[0],
    #         employment_type=models.Profile.RELIGION[0],
    #         annual_income=models.Profile.RELIGION[0],
    #         country=models.Profile.RELIGION[0],
    #         state=models.Profile.RELIGION[0],
    #         city=models.Profile.RELIGION[0],
    #         citizenship=models.Profile.RELIGION[0],
    #         family_value=models.Profile.RELIGION[0],
    #         family_type=models.Profile.RELIGION[0],
    #         family_status=models.Profile.RELIGION[0],
    #         father_occupation=models.Profile.RELIGION[0],
    #         mother_occupation=models.Profile.RELIGION[0],
    #         no_of_brothers=models.Profile.RELIGION[0],
    #         brothers_married=models.Profile.RELIGION[0],
    #         no_of_sisters=models.Profile.RELIGION[0],
    #         sisters_married=models.Profile.RELIGION[0],
    #         ancestral_origin='Parsi',
    #         about_family='Middle class family staying in Bangalore',
    #         hobbies=models.Profile.RELIGION[0],
    #         interests=models.Profile.RELIGION[0],
    #         favourite_music=models.Profile.RELIGION[0],
    #         favourite_reads=models.Profile.RELIGION[0],
    #         preferred_movies=models.Profile.RELIGION[0],
    #         sports_and_fitness=models.Profile.RELIGION[0],
    #         favourite_cuisine=models.Profile.RELIGION[0],
    #         preferred_dress_style=models.Profile.RELIGION[0],
    #         spoken_languages=models.Profile.RELIGION[0],
    #         pref_age=models.Profile.RELIGION[0],
    #         pref_height=models.Profile.RELIGION[0],
    #         pref_martital_status=models.Profile.RELIGION[0],
    #         pref_phy=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #         hobbies=models.Profile.RELIGION[0],
    #
    #     )
