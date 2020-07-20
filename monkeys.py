word = "monkeys"
mid_line = "One fell down and bump his head"
last_line = "NO MORE monkeys jumping on the bed"

for num in range(5,0,-1):

    if num == 1:
        word = "monkey"

    if num > 0:    
        print(str(num) + " little " + word + " jumping on the bed")
        print(mid_line)
        if num == 1:
            print(last_line)

    print("la la la la la la la")
    print("=====================")

        
