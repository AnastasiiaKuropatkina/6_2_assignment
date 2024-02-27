import csv
from convertor.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from convertor.distance import feet_to_meters, meters_to_feet 


def convert_temperatures(input_file, output_file, target_dis, target_unit):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            date, distance, reading = row
            reading_value, reading_unit = reading[:-2], reading[-1:]
            distance_unit = distance[-1:]
            match (target_unit, reading_unit):
                case ('C', 'F'):
                    converted = fahrenheit_to_celsius(float(reading_value))
                    new_reading = f'{converted:.0f}°C'
                case ('F', 'C'):
                    converted = celsius_to_fahrenheit(float(reading_value))
                    new_reading = f'{converted:.0f}°F'
                case _:
                    new_reading = reading
            match (target_dis, distance_unit):
                case ('m', 't'):
                    converted_dis = feet_to_meters(float(distance[:-2]))
                    new_dis = f'{converted_dis:.0f}m'
                case ('ft', 'm'):
                    converted_dis = meters_to_feet(float(distance[:-2]))
                    new_dis = f'{converted_dis:.0f}ft'
                case _:
                    new_dis = distance
            writer.writerow([date, new_dis, new_reading])


# Example usage:
convert_temperatures('input.csv', 'output.csv', 'm', 'C')