import re

four_digits = re.compile(r"^\d{4}$")
nine_digits = re.compile(r"^\d{9}$")
height_inches = re.compile(r"^\d{1,}in$")
height_centimeters = re.compile(r"^\d{1,}cm$")
valid_colour = re.compile(r"^#[a-fA-F0-9]{6}$")
