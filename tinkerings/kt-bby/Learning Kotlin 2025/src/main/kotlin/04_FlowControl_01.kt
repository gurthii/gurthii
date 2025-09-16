// admit with gift or not plus under age

fun main(){
    println("What's your name? ")
    val name = readln()
    println("How old are you? ")
    val user_age = readln().toInt()

    println(admitOne(user_age, name))
    val turnState = true
    if (turnState) {
       println("Yes, turned on")
    } else {
        println("No, turned off")
    }
    // this also works if() "" else ""
}

fun admitOne(user_age: Int, name: String):String {
    val somn = when {
        user_age >= 16 -> "over 16, $user_age years old"
        user_age < 16 -> "you are way too young to be out here"
        else           -> "this is unexpected"
    }

    return somn
}