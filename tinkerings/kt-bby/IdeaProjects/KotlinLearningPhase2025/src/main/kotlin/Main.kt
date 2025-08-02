import java.util.Scanner
import kotlin.math.sqrt
import kotlin.math.pow

fun main() {
    // Learning Sprint #1
    // assignment/initialization is required before printing a declared variable
    val isTrue: Boolean
    // println(isTrue) // will trigger an error
    isTrue = false
    println(isTrue)

    /*
    var isFalse // you must declare type to allow future assignment/initialization;
    // type inference fails because kotlin has no context
    isFalse = false
    println(isFalse)
     */

    // use backticks if you have to use a space in your variable name
    var `hello guy` = "Some guy"
    println(`hello guy`)

    // data types and their sizes
    println("Short: Min ${Short.MIN_VALUE}, Max ${Short.MAX_VALUE}\nByte: Min ${Byte.MIN_VALUE}, Max ${Byte.MAX_VALUE}")
    println("Type ${999_999_999_999_999_999::class.simpleName}")

    // output in one sentence
    print(`hello guy`)
    print(isTrue)

    // calling a function
    somnText()

    // Learning Sprint #2
    var scanner_ = Scanner("one two three four five")
    println(scanner_.next()) // prints single word

    scanner_ = Scanner("Hello-Kotlin")
    scanner_.useDelimiter("-")
    println(scanner_.next())
    println(scanner_.next())

    scanner_ = Scanner("hello 123")
    println(scanner_.next())
    var num = scanner_.nextInt().toInt()
    num += 5
    num *= 2
    println(num)
    scanner_.close()

    // Learning Sprint #3
    // 2. Print messages
    println("Use the val keyword when the value doesn't change." )
    println("Use the var keyword when the value can change.")
    println("When you define a function, you define the parameters that can be passed to it." )
    println("When you call a function, you pass arguments for the parameters.")

    // 3. Fix compile error
    // fun main() {
    //    println("New chat message from a friend'}
    // }
    println("New chat message from a friend")

    // 4. String templates
    var discountPercentage: Int = 0 // swapped the val for var to allow re-assignment below;
    // SOLUTION: However, their values are immutable in the context of the program, so you can stick with the val keyword.
    var offer: String = "" // swapped the val for var to allow re-assignment below
    val item = "Google Chromecast"
    discountPercentage = 20
    offer = "Sale - Up to $discountPercentage% discount on $item! Hurry up!"
    println(offer)

    // 5. String concatenation
    val numberOfAdults = 20 // switched str variables to int
    val numberOfKids = 30 // switched str variables to int
    val total = numberOfAdults + numberOfKids
    println("The total party size is: $total")

    // 6. Message formatting
    val baseSalary = 5000
    val bonusAmount = 1000
    var totalSalary: Int
    /*
     * refactored above expression by first initializing it and giving it a type
     * output a summation instead of string template, and
     * removing the quotation marks and string templates
     */
    totalSalary = baseSalary + bonusAmount
    println("Congratulations for your bonus! You will receive a total of $totalSalary (additional bonus).")

    // 7. Implement basic math operations
    // requires definition of add() function
    val firstNumber = 10
    val secondNumber = 5
    val thirdNumber = 8
    val result_ = add(firstNumber, secondNumber)
    val anotherResult = add(firstNumber, thirdNumber)
    val subResult = subtract(nthNumber = firstNumber, mthNumber = thirdNumber)
    println("$firstNumber + $secondNumber = $result_")
    println("$firstNumber + $thirdNumber = $anotherResult")
    println("$firstNumber - $thirdNumber = $subResult")

    // 8. Default parameters
    // requires definition of displayAlertMessage()
    val operatingSystem = "Chrome OS"
    val emailId = "sample@gmail.com"
    println(displayAlertMessage(operatingSystem, emailId))

    // part 2, test for default parameters
    val firstUserEmailId = "user_one@gmail.com"
    println(displayAlertMessage(emailId = firstUserEmailId))
    println()
    val secondUserOperatingSystem = "Windows"
    val secondUserEmailId = "user_two@gmail.com"
    println(displayAlertMessage(secondUserOperatingSystem, secondUserEmailId))
    println()
    val thirdUserOperatingSystem = "Mac OS"
    val thirdUserEmailId = "user_three@gmail.com"
    println(displayAlertMessage(thirdUserOperatingSystem, thirdUserEmailId))
    println()

    // 9. Pedometer
    val steps = 4000
    val caloriesBurned = pedometerStepsToCalories(steps);
    println("Walking $steps steps burns $caloriesBurned calories")

    // 10. Compare two numbers
    var timeSpentToday: Int
    var timeSpentYesterday: Int
    timeSpentToday = 300
    timeSpentYesterday = 250
    println(compareNumeros(timeSpentToday, timeSpentYesterday)) // should return true

    timeSpentToday = 300
    timeSpentYesterday = 300
    println(compareNumeros(timeSpentToday, timeSpentYesterday)) // should return false

    timeSpentToday = 200
    timeSpentYesterday = 220
    println(compareNumeros(timeSpentToday, timeSpentYesterday)) // should return false
    println()

    // 11. Move duplicate code into a function
    println(cityWeather(cityName = "Ankara", lowTemps = 27, highTemps = 31, rainChance = "82%"))
    println()
    println(cityWeather(cityName = "Tokyo", lowTemps = 32, highTemps = 36, rainChance = "10%"))
    println()
    println(cityWeather(cityName = "Cape Town", lowTemps = 59, highTemps = 64, rainChance = "2%"))
    println()

    things()
    // Learning Sprint #4
    // data types in kotlin
    val aChar: Char = 'a' // Char, only stores a single character, use single quotes to escape Kotlin inferring it as a string
    val aStringer: String = "Hello \nWorld!"

    // another way to declare val variables?
    val myName: String = "Joey"
    val myAge: Int = 90

    // type inference vs floating point numbers
    val pencilDiameter = 0.7 // inferred to be a Double, for consistency with Java and higher precision
    val penDiameter = 0.8F // explicitly declared as a Float

    // declaring big numbers in a readable manner
    var mySalary: Int = 10_000_000

    // basic print line formats
    println("My name is $myName. \nI earn a salary of ${mySalary * 1} annually.")
    println("This worked too, $myName and pie is $NUM_PIE.")
    println(aChar::class.simpleName) // checking the data type variableName::class.simpleName
    println(aStringer.length) // checks length of variable, but may not always work for null variables
    println("Pen and pencil diameters $penDiameter & $pencilDiameter \nData types: ${penDiameter::class.simpleName} & ${pencilDiameter::class.simpleName}")
    println(getSomeCookies(myName, myAge))
    println(getSomeCookies(myName = "Kim")) // named argument
    println(getSomeCookies()) // prints default arguments
    // Learning Sprint #5
    // Using Java's scanner
    println("..expecting input in console")
    var scanner = Scanner("124")// Scanner(System.`in`) // expects some input in the console
    println(scanner.nextLine())

    scanner = Scanner("Ariel is 10 years old.")
    println(scanner.hasNextInt()) // checks if there's an int, else returns false - most useful in an if/else statement.
    println(scanner.next()) // prints next string/line?
    println(scanner.hasNext()) // catches error, useful in an if/else statement

    println("Done.")

    // Strings
    val newStateUnlocked = "New York"
    println(newStateUnlocked.length) // checks the string length
    println((newStateUnlocked + "\n").repeat(3)) // repeats printing string n times

    var myMotto = """We we ngima,
nene 
muno
    """.trimIndent() // removes first/last line and trims indents
    println(myMotto)
    println(newStateUnlocked.reversed()) // reverses string
    println('0' + "1" + '2' + 3)
    println("Kot lin".length)

    // Arithmetic Operations
    println(1/2) // returns 0. only considers division of integers, so fractional/decimals are discarded
    println(2%3) // returns 2. modulus returns the remainder after division

    println("input a number to square: ")
    val input = 25 // readLine()!!.toInt()
    val result = sqrt(input.toDouble())
    println("the square of $input is $result.")

    val base = 2.toDouble()
    val exponent = 3.toDouble()

    println("Using the .pow method with base $base and exponent $exponent, i.e., " +
            "${base.toInt()}^${exponent.toInt()} results in: ${base.pow(exponent)}")
    var a = 10
    println("a-- prints original a value: ${a--}, then decrements a by 1 and reassigns it the new value($a)")
    a = 10
    println("--a first decrements a by 1 to get ${--a}, then re-assigns it to a resulting in: ${a}")

    a = 10
    var b = a-- // b gets 10, a is decreased to 9
    println("in an expression, b = a--, b gets original  value of a ($b) and a is decreased by 1 and re-assigned to said value: $a")

    a = 10
    b = --a // a is decreased first then assigned to b, b gets 9
    println("in an expression, b = --a, a is first decreased by 1 ($a) then assigned to b: $b")

    // Learning Sprint #6
    


}

fun somnText() {
    print("Kotlin is a modern programming language.")
    print("I will finish studying Kotlin in ")
    print(2024)
    println("!")
    println()
}
// the add function for problem 7
fun add(nthNumber: Int, mthNumber: Int) : Int {
    return  nthNumber + mthNumber
}
fun subtract(nthNumber: Int, mthNumber: Int) : Int {
    return nthNumber - mthNumber
}
// the displayAlertMessage() function for problem 8
fun displayAlertMessage(operatingSystem: String = "Unknown OS", emailId: String) : String {
    return "There's a new sign-in request on $operatingSystem for your Google Account $emailId."
}
// formatting for problem 9
fun pedometerStepsToCalories(numberOfSteps: Int): Double {
    val caloriesBurnedForEachStep = 0.04
    val totalCaloriesBurned = numberOfSteps * caloriesBurnedForEachStep
    return totalCaloriesBurned
}
// for problem 10
fun compareNumeros(timeSpentToday: Int, timeSpentYesterday: Int) : Boolean {
    return timeSpentToday > timeSpentYesterday
}
// for problem 11
fun cityWeather(cityName: String, lowTemps: Int, highTemps: Int, rainChance: String) : String {
    return """
    City: $cityName
    Low temperature: $lowTemps, High temperature: $highTemps
    Chance of rain: $rainChance
    """.trimIndent()
}
fun things() : Unit {
    // Functions with a return type of Unit don't have to include a return statement.
    println("hi")
}
/*
 * This is a block (multi-line) comment,
 * Perfect for comments beyond 100 characters.
 */
const val NUM_PIE = 3.145 // const modifier, must be declared top level outside any functions
// how to declare a function, callable in the main fun (entry point)
fun getSomeCookies(myName: String = "John Doe", myAge: Int = 100) : String{ // includes default arguments
    return "$myName did not in fact get some cookies :( and you are $myAge years old."
}
/*
 * detailed example of a function:
 * fun myFunction(parametername: datatype): returntype {
 *     return parametername
 * }
 *
 * in main():
 * println(
 */