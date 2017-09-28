unit_rates = {
    "weight": [
        "gm", "lbs", 0.002216], "distance": [
            "mi", "km", 1.6], "volume": [
                "l", "fl", 33.814], "length": [
                    "in", "cm", 2.54]}


class Conversion:

    @staticmethod
    def convert(measurement, value, unit):
        factor = unit_rates[measurement][2]
        unit1 = unit_rates[measurement][0]
        unit2 = unit_rates[measurement][1]
        if unit == unit1:
            return "{:.2f} {}".format((value * factor), unit2)
        else:
            return "{:.2f} {}".format((value / factor), unit1)

    @staticmethod
    def convert_temp(value, unit):
        if unit == "F":
            return "{:.2f} C".format((value - 32) * 0.5556)
        else:
            return "{:.2f} F".format((value / 0.5556) + 32)

print(Conversion.convert("distance", 3541, "km"))
print(Conversion.convert("weight", 66000, "lbs"))
print(Conversion.convert("volume", 1000, "l"))
print(Conversion.convert("length", 177, "cm"))
print(Conversion.convert_temp(37, "C"))
