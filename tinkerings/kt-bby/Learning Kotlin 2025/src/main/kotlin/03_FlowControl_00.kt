fun main() {
                                                          // CONDITIONALS
    val temp = 20

    val goldilocksReaction = when {                       // when here is an expression that can be stored in a variable
        temp > 55 -> "hot"                                // temp > 55 is a conditional w/ comparison operators; results to a boolean
        temp < 40 -> "cold"                               // values after arrow -> like "hot" are returned if condition returns true
        else      -> "jus right!"
    }
    println(goldilocksReaction)                           // when is evaluated top-down; wherever true is returned code execution stops there
    println(goldilocksReaction::class.simpleName)         // when result is a string

    val scam = "scam"
    var isScam = when {
        scam == "scam" -> "yep"
        scam == "nope" -> "not scam"
        else           -> "idk"
    }
    println(isScam)

    isScam = when(scam) {                                 // when can also be refined by adding a subject (expression or variable)
        "scam" -> "yep"
        "nope" -> "not yep"
        else   -> "idk"
    }
    println(isScam)

    var lightBulbState = false
    var isBulbOn =                                      // if checking a few conditionals, use 'if' else 'when' is more robust
        if (lightBulbState) {
            lightBulbState = false
            "i've turned off the light"
        } else {                                        // an 'else if' expression is also acceptable here
            lightBulbState = true
            "nimewasha taa boss"

        }
    println(isBulbOn)
    var wattage = 0
    if (lightBulbState) {                               // as a statement, else statement is not necessary
        wattage += 1
    }
    println(wattage)
}