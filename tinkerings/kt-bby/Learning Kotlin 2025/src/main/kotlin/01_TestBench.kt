import kotlin.math.sqrt
import kotlin.math.pow

fun main() {
    print("What is your name?: ")
    val userName = readln()
    print("Input the base: ")
    val base = readln().toFloat()
    print("Input the exponent: ")
    val exp = readln().toFloat()
    print("Input the number you want to get the root of: ")
    val getSqrt = readln().toDouble()

    println(mathOps(base, exp, getSqrt, userName))

    println("got invite (*expecting boolean)? ")
    val invitation = readLine().toBoolean() // read other value in the same way
    println("got gift (*expecting boolean)? ")
    val hasGift = readLine().toBoolean()
    println(invitation)
    println(hasGift)
    println("Guest has invitation and gift: ${invitation && hasGift}.")
    // write your code here


}

fun mathOps(base: Float, exp: Float, getSqrt: Double, userName: String): String {
    val power = base.pow(exp)
    val squareroot = sqrt(getSqrt)

    return "Hey $userName, please note that:\n" +
            "${base.toInt()} to the power of ${exp.toInt()} = ${power.toInt()}\n" +
            "square root of ${getSqrt.toInt()} = ${squareroot.toInt()}"
}