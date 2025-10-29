class Circle(var radius: Double) {
    public val pi = Math.PI // variable will only be visible in this class, any code outside the class can't see the property
    val circumference: Double = 2 * pi * radius

}

class Rectangle(var length: Double, var height: Double){
    fun area() = length * height
    fun perimeter() = 2 * (length + height)
}

fun main () {
    val aCircle = Circle(10.0) // constructing an object
    println(aCircle.radius)
    println(aCircle.circumference)

    val aRectangle = Rectangle(10.0, 20.0)
    println(aRectangle.perimeter())
    println(aRectangle.area())
}