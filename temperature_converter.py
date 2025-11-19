"""Temperature converter between Celsius, Fahrenheit, and Kelvin."""

from __future__ import annotations


ABS_ZERO_C = -273.15


def convert_temperature(value: float, unit: str) -> dict[str, float]:
    """Convert input temperature into Celsius, Fahrenheit, and Kelvin."""
    normalized_unit = unit.strip().lower()

    if normalized_unit in {"c", "celsius"}:
        celsius = value
    elif normalized_unit in {"f", "fahrenheit"}:
        celsius = (value - 32.0) * 5.0 / 9.0
    elif normalized_unit in {"k", "kelvin"}:
        if value < 0:
            raise ValueError("Kelvin values cannot be negative.")
        celsius = value - 273.15
    else:
        raise ValueError(
            "Unknown unit. Please use Celsius, Fahrenheit, or Kelvin."
        )

    if celsius < ABS_ZERO_C:
        raise ValueError("Temperature is below absolute zero.")

    fahrenheit = celsius * 9.0 / 5.0 + 32.0
    kelvin = celsius + 273.15

    return {
        "celsius": celsius,
        "fahrenheit": fahrenheit,
        "kelvin": kelvin,
    }


def main() -> None:
    """Prompt user for input and display converted temperatures."""
    try:
        value = float(input("Enter the temperature value: ").strip())
    except ValueError:
        print("Temperature must be a numeric value.")
        return

    unit = input(
        "Enter the original unit (Celsius/Fahrenheit/Kelvin): "
    ).strip()

    try:
        converted = convert_temperature(value, unit)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print("\nConverted values:")
    print(f"- Celsius: {converted['celsius']:.2f} °C")
    print(f"- Fahrenheit: {converted['fahrenheit']:.2f} °F")
    print(f"- Kelvin: {converted['kelvin']:.2f} K")


if __name__ == "__main__":
    main()

