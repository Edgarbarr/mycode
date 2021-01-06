#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
def heyNotTooRough():
    for farm in farms:
        if farm["name"] == "NE Farm":
            print(farm["agriculture"])
heyNotTooRough()

def hurtMePlenty():
    userFarm = input("Choose a farm?\nNE Farm, W Farm, SE Farm\n")
    for farm in farms:
        if farm["name"] == userFarm:
            print(farm["agriculture"])
hurtMePlenty()

def nightmare():
    userFarm = input("Choose a farm?\nNE Farm, W Farm, SE Farm\n")
    for farm in farms:
        if farm["name"] == userFarm:
            onlyAnimals = filter(lambda thing: thing != "carrots" and thing != "celery", farm["agriculture"])
            print(list(onlyAnimals))
nightmare()
