# ColorfulCLI

## A simple way to add color to your Python CLI apps.


#
# Example uses:

## Import the module:

	from ColorfulCLI import colorful

## Create an instance of the ColorfulCLI class

	color = Colorful()

## Example usage
	print(f"{color.yellow}Hello, World!{color.reset}")

	print(f"{color.blink}{color.yellow}{color.red_bg}Hello, world!{color.reset}")

	print_colored_text("Hello, World!", "yellow")

	print_colored_text("This is a test.", "red")

	print_colored_text("The sky is blue.", "blue")

	print_colored_text("I love Python.", "white")

##
# Caveats:

 Not all escape codes work with all terminals. Be sure to test your terminal with the styles you  would like to use.