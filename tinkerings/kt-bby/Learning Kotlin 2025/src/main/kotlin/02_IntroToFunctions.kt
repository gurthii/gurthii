fun main(){
    println("kotlin is statically typed: once we've declared a variable with a particular data type, no other type " +
            "of value can go into it.")
                                                           // FUNCTIONS
    println(greetings("Kinothia", 92))                     // positional arguments (passed in the same order as fn paras)
    println(greetings(age = 30, username = "Shuqo"))       // you can assign your arguments like this too aka named arguments

    val n = 20.90                                          // type inference in action, ctrl+q to see what ide inferred
    println(n::class.simpleName)                           // how to get the data type in simple language

    println(circum(2.0))                                  // calling/invoking a function; you may also save result in a var first
    print(speed(321.8, 4))

}
// sample function with a block body (allowing for a code block with statements)
fun greetings(username: String, age: Int): String{        // data type for input/output must be specified
    return "Hello $username, you're $age years old?"      // username/age are parameters
}
const val pi = 3.14                                       // type inference works here for the return types (ideal for simple fns w/ expressions)
fun circum(radii: Double) = 2 * pi * radii                // shorter way of writing a function using just an expression
fun speed(distance: Double,time: Int=1) = distance / time // 1 is a default argument, use named arguements if first para is to be defaulted
// if return type is omited for a function with a block body, 'Unit' type is auto returned

