
BEGIN {
    FS = "::";
    VALUE = 0;
    WORD = ""
    DEF = "";
}
{
    if (NF <=1 && VALUE == 1) {
        if(WORD == "Description") {
            printf("%s",DEF);
            exit 0;
        }
        VALUE = 0;
    } else if (NF == 2) {
        # If new definition
        if ($1 != "") {
            # Clean up old definition
            if (VALUE == 1) {
                if (WORD == "Description") {
                    printf("%s",DEF);
                    exit 0;
                }
                VALUE = 0;
            }
            # New Definition
            WORD = $1;
            DEF = $2;
        } else if(VALUE == 1) {
            DEF=DEF $2;
        }
        VALUE = 1;
    }
}
END{}
