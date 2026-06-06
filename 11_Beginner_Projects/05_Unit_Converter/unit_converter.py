"""
Project 5: Unit Converter

Convert between different units of measurement.
"""

def convert_length(value, from_unit, to_unit):
    """Convert length units. All conversions go through meters."""
    to_meters = {
        "mm": 0.001, "cm": 0.01, "m": 1.0,
        "km": 1000.0, "in": 0.0254, "ft": 0.3048,
        "yd": 0.9144, "mi": 1609.344
    }
    if from_unit not in to_meters or to_unit not in to_meters:
        raise ValueError(f"Unknown unit. Valid: {list(to_meters.keys())}")
    meters = value * to_meters[from_unit]
    return meters / to_meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    """Convert weight units. All conversions go through kilograms."""
    to_kg = {
        "mg": 0.000001, "g": 0.001, "kg": 1.0,
        "t": 1000.0, "oz": 0.028349, "lb": 0.453592
    }
    if from_unit not in to_kg or to_unit not in to_kg:
        raise ValueError(f"Unknown unit. Valid: {list(to_kg.keys())}")
    kg = value * to_kg[from_unit]
    return kg / to_kg[to_unit]

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    # Convert to Celsius first
    if from_unit == "C": celsius = value
    elif from_unit == "F": celsius = (value - 32) * 5/9
    elif from_unit == "K": celsius = value - 273.15
    else: raise ValueError("Valid units: C, F, K")
    
    # Convert from Celsius to target
    if to_unit == "C": return celsius
    elif to_unit == "F": return celsius * 9/5 + 32
    elif to_unit == "K": return celsius + 273.15
    else: raise ValueError("Valid units: C, F, K")

def main():
    print("=" * 40)
    print("     🔄 UNIT CONVERTER")
    print("=" * 40)
    
    converters = {
        "1": ("Length",      convert_length,      "mm, cm, m, km, in, ft, yd, mi"),
        "2": ("Weight",      convert_weight,      "mg, g, kg, t, oz, lb"),
        "3": ("Temperature", convert_temperature, "C, F, K"),
    }
    
    while True:
        print("\nCategories:")
        for key, (name, _, units) in converters.items():
            print(f"  {key}. {name} ({units})")
        print("  4. Quit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "4":
            print("Goodbye!")
            break
        
        if choice not in converters:
            print("Invalid choice.")
            continue
        
        name, converter, units = converters[choice]
        print(f"\n{name} Converter — Units: {units}")
        
        try:
            value = float(input("Enter value: "))
            from_unit = input("From unit: ").strip()
            to_unit = input("To unit: ").strip()
            
            result = converter(value, from_unit.lower() if name != "Temperature" else from_unit.upper(),
                             to_unit.lower() if name != "Temperature" else to_unit.upper())
            
            print(f"\n✅ {value} {from_unit} = {result:.6g} {to_unit}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
