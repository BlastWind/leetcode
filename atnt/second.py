from os import path
from collections import defaultdict
from typing import DefaultDict, TypedDict


def more_recent_than(date1: str, date2: str) -> bool:
    """
    returns if date1 is more recent than date2
    """
    [date1Month, date1Day, date1Year] = date1.split("/")
    [date2Month, date2Day, date2Year] = date2.split("/")

    if date1Year > date2Year:
        return True
    if date1Year == date2Year:
        if date1Month > date2Month:
            return True
    if date1Year == date2Year and date1Month == date2Month:
        if date1Day > date2Day:
            return True

    return False


model_info = {
    "Camry": {"make": "Toyota", "speed": 100},
    "Prius": {"make": "Toyota", "speed": 80},
    "Corvette": {"make": "chevrolet", "speed": 160},
    "Challenger": {"make": "dodge", "speed": 155},
}


def doProject(input: list) -> str:
    """
    Output the message `OWNER has TOTAL vehicles and is currently driving a YEAR-OF-PRODUCTION MAKE MODEL that goes SPEED`,
    where the `OWNER` is the owner with the most vehicles (on tie, the first max owner that appears in the list is chosen)
    and the `MODEL` is their most recent model.
    """

    # TODO CLARIFY #1: What if empty list? Or ill format in general?
    if not input:
        return 'Please input a list of vehicle informations. Example vehicle entry: "Challenge,12/01/2018,Sam".'

    class DriverCacheEntry(TypedDict):
        carsOwned: int
        newestModel: str
        newestModelDop: str

    defaultDriverCacheEntry: DriverCacheEntry = {
        "carsOwned": 0,
        "newestModel": "",
        "newestModelDop": "",
    }
    driver_cache: DefaultDict[str, DriverCacheEntry] = defaultdict(
        lambda: defaultDriverCacheEntry.copy()
    )

    for item in input:
        # MODEL,DATE OF PRODUCTION,OWNER
        [curModel, curDop, owner] = item.split(",")
        driver_cache[owner]["carsOwned"] += 1

        if driver_cache[owner]["newestModel"]:
            # Compares dop, override prevTopModel if curModel is faster
            prevNewestModelDop = driver_cache[owner]["newestModelDop"]
            if more_recent_than(
                curDop, prevNewestModelDop
            ):  # TODO CLARIFY #2: What if two cars same date?
                driver_cache[owner]["newestModel"] = curModel
                driver_cache[owner]["newestModelDop"] = curDop
        else:
            # No entry yet, enlist current
            driver_cache[owner]["newestModel"] = curModel
            driver_cache[owner]["newestModelDop"] = curDop

    # Get driver with most car and their info
    carHoarder = max(
        driver_cache.items(),  # TODO CLARIFY #3: What if two drivers shared max?
        key=lambda driver_data: driver_data[1]["carsOwned"],
    )[0]
    carHoarderCarsOwned = driver_cache[carHoarder]["carsOwned"]
    carHoarderNewestModel = driver_cache[carHoarder]["newestModel"]
    carHoarderNewestModelMake = model_info[carHoarderNewestModel]["make"]
    carHoarderNewestModelSpeed = model_info[carHoarderNewestModel]["speed"]
    carHoarderNewestModelDateOfProduction = driver_cache[carHoarder]["newestModelDop"]
    carHoarderNewestModelYearOfProduction = (
        carHoarderNewestModelDateOfProduction.rsplit("/")[-1]
    )

    return (
        f"{carHoarder} has {carHoarderCarsOwned} vehicles and is currently driving a "
        f"{carHoarderNewestModelYearOfProduction} {carHoarderNewestModelMake} {carHoarderNewestModel} "
        f"that goes {carHoarderNewestModelSpeed} mph."
    )


if __name__ == "__main__":
    testFile = path.join("input.txt")

    input = []
    with open(testFile, "r") as fr:
        input = [line.strip() for line in fr if line != "\n" and line[0] != "#"]

    output = doProject(input)
    print(output)
