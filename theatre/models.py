from django.db import models

# Represents an actor with a first and last name
class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Represents a stage where performances take place
class Stage(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# Represents a director of a performance
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Represents a performance in the theatre
class Performance(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='performances')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"


# Represents a role in a performance
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Links an actor to a role in a specific performance
class Casting(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor} jako {self.role} v {self.performance}"



