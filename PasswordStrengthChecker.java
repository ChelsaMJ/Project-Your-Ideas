import java.util.Scanner;

public class PasswordStrengthChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a password: ");
        String password = scanner.nextLine();

        int strength = checkPasswordStrength(password);

        switch (strength) {
            case 1:
                System.out.println("Password is very weak. Please make it stronger.");
                break;
            case 2:
                System.out.println("Password is weak. Consider adding more complexity.");
                break;
            case 3:
                System.out.println("Password is moderate. Good job!");
                break;
            case 4:
                System.out.println("Password is strong!");
                break;
            default:
                System.out.println("Invalid password.");
        }

        scanner.close();
    }

    public static int checkPasswordStrength(String password) {
        int strength = 0;

        // Check length
        if (password.length() >= 8) {
            strength++;
        }

        // Check for uppercase and lowercase letters
        if (hasUppercase(password) && hasLowercase(password)) {
            strength++;
        }

        // Check for digits
        if (hasDigit(password)) {
            strength++;
        }

        // Check for special characters
        if (hasSpecialCharacter(password)) {
            strength++;
        }

        return strength;
    }

    public static boolean hasUppercase(String password) {
        return !password.equals(password.toLowerCase());
    }

    public static boolean hasLowercase(String password) {
        return !password.equals(password.toUpperCase());
    }

    public static boolean hasDigit(String password) {
        return password.matches(".*\\d.*");
    }

    public static boolean hasSpecialCharacter(String password) {
        return !password.matches("[A-Za-z0-9]*");
    }
}
