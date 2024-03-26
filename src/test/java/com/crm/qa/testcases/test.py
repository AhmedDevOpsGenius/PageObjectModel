import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class SeleniumTest {
    public static void main(String[] args) {
        // Set the path to the ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");

        // Create a new instance of the Chrome driver
        WebDriver driver = new ChromeDriver();

        // Navigate to a website
        driver.get("https://www.example.com");

        // Get and print the title of the current page
        String pageTitle = driver.getTitle();
        System.out.println("Page title is: " + pageTitle);

        // Verify the title of the page
        if (pageTitle.equals("Example Domain")) {
            System.out.println("Title verification successful");
        } else {
            System.out.println("Title verification failed");
        }

        // Close the browser
        driver.quit();
    }
}
