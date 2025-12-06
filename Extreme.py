# 🧠 Advanced Python Challenge: "Smart Cinema Ticketing System"
# Difficulty: EXTREME 🔥🔥🔥
# ------------------------------------------------------------


# 🎟️ GIVEN DATA (DO NOT EDIT)
movies = ["Dune 2", "Inside Out 2", "Gladiator 2", "Joker 2", "Wicked"]
ticket_prices = [200, 180, 250, 220, 190]
zipped_list_of_films=zip(movies, ticket_prices)
available_films=[]
sold_out_films=[]


#Generates available_films with 10 free seats for each movie
for i in zipped_list_of_films:
    movie, cost= i
    available_films.append([movie, cost, ["O" for i in range(10)]])

#DISPLAYS

#prints UPDATED available films
def list_available_films(available_films):
    count=0
    if len(available_films)==0:
        print("No more movies available")
    else:
        for index in range(len(available_films)):
            chosen_film, chosen_film_seats, available_seats, price=variables(available_films, index)
            if available_seats==0:
                continue
            else:
                string=f"- {chosen_film}- {available_seats} Seats Available - {price} EGP"
                count+=1
                print(str(count) + string )

#print seating chart of selected film
def show_seating_chart(chosen_film, chosen_film_seats):
    string=""
    print(f"\nSeating chart for {chosen_film}")
    for i in chosen_film_seats:
        string+=i+" "
    print(string)

#return most_available_seats_films
#to use solely in Final Goodbye Function below- Prints the message before goodbye & available films with most available seats
def most_available_seats_films():
    count_list=[]
    strings=[]
    most_available_seats_list=[]
    for index in range(len(available_films)):
        chosen_film, chosen_film_seats, available_seats, price=variables(available_films, index)
        count_list.append(available_seats)
    for index in range(len(count_list)):
        if count_list[index]==max(count_list):
            chosen_film, chosen_film_seats, available_seats, price = variables(available_films, index)
            most_available_seats_list.append([chosen_film, price, chosen_film_seats])
            strings.append(f"- {chosen_film} - Ticket: {price} EGP - {available_seats} Seats available!")
    for order, string in enumerate(strings, start=1):
        print(order, string)
    return most_available_seats_list

#returns chosen_film, chosen_film_seats, available_seats, price
def variables(available_films, index):
    chosen_film = available_films[index][0]
    chosen_film_seats = available_films[index][2]
    available_seats = chosen_film_seats.count("O")
    price=available_films[index][1]
    return chosen_film, chosen_film_seats, available_seats, price

#CHECKERS

#Returns a positive number or "done"
def positive_numbers_only(answer):
    while True:
        try:
            if int(answer) > 0: return int(answer)
            else: answer=input("Enter positive Numbers Only or (done) to exit: ")
        except ValueError:
            if not answer.lower().strip()=="done": answer=input("Enter Numbers Only or (done) to exit: ")
            else: return "done"

#Returns Cheapest Ticket Price
def cheapest_ticket():
    prices=[]
    for index in range(len(available_films)): prices.append(available_films[index][1])
    return min(prices)



#Returns Index or Done
def pick_a_film(available_films):
    answer = input("\nPlease select a film by number or name: ")
    while True:
        try:
            index = int(answer) - 1
            if index in range(len(available_films)):
                return index
            else:
                answer = input(f"Numbers from 1-{len(available_films)} Only Please or (Done) to Exit!")
        except ValueError:
            for index in range(len(available_films)):
                if answer.lower().strip() == available_films[index][0].lower().strip():
                    return index
            if answer.lower().strip() == "done":
                return "done"
            else:
                answer = input("Invalid! Please Enter a number or (Done) to Exit!: ")

#ACTION: Replace available films with most available films when selecting which film here.
#Returns index or done
def before_quitting():
    print("\nBefore you leave us, Take a look at the movies with the most available seats: \n")
    most_available_seats_list=most_available_seats_films()
    question=again("\nDo you want to select a movie from the above? Y/N ")
    if not question=="done":
        if question:
            index = pick_a_film(most_available_seats_list)
            if index=="done": return "done"
            return index
        else:
            return "done"
    else:
        return "done"


# ACTIONS
# Update the seats in available_films.  returns available_films
def update_seats(chosen_film_seats, tickets, index):
    for e in range(tickets):
        for i in range(len(chosen_film_seats)):
            if chosen_film_seats[i] == "O":
                chosen_film_seats[i] = "X"
                break
    available_films[index][2] = chosen_film_seats
    return available_films

# universal again, returns True or False or "done"
def again(question):
    answer = input(question)
    while True:
        try:
            answer = int(answer)
            answer = input("Y, N or Done to Quit: ")
        except ValueError:
            answer = answer.lower().strip()
            if answer in ["y", "yes"]:
                return True
            elif answer in ["n", "no"]:
                return False
            elif answer == "done":
                return "done"
            else:
                answer = input("Yes, No or Done to Quit: ")



#Returns tickets or Done or "select another film"
def pick_tickets_available_seats(chosen_film, available_seats):
    answer = input(f"\nHow many tickets do you want to buy for {chosen_film}?")
    while True:
        tickets = positive_numbers_only(answer)
        if tickets == "done": return "done"
        if tickets > available_seats:
            answer = again(
                f"\nNo Enough Seats. Only {available_seats} tickets available, do you want to buy less tickets? Y/N")
            if answer == "done":
                return "done"
            else:
                if answer:
                    answer = input(
                        f"\nHow many tickets do you want to buy for {chosen_film}, (Maximum {available_seats} Seats Available)? ")
                else:
                    answer = again(f"\nDo you want to select a different film? Y/N")
                    if answer == "done":
                        return "done"
                    else:
                        if answer:
                            return "select another film"
                        else:
                            return "done"
        else:
            return tickets


# returns "done" or int(budget+current_budget) as a positive number
def enter_budget(current_budget=0):
    count=0
    while True:
        entry = positive_numbers_only(input(f"\nYour current budget is {current_budget}, How much do you want to add? "))
        if entry == "done":
            count+=1
            if count>1: return "done"
            print("\nBefore you leave us, Take a look at the movies with the most available seats: \n")
            most_available_seats_films()
            question = again("\nDo you want to add more budget? Y/N ")
            if question == "done": return "done"
            else:
                if question:
                    continue
                else:
                    return "done"
        else:
            budget = entry + current_budget
            if budget=="done": return "done"
            return budget


#Returns "done" / "select another film" / updated enough current_budget
def make_budget_enough(current_budget, this_cost=cheapest_ticket()):
    if current_budget=="done": return "done"
    budget=current_budget
    while True:
        remaining=(budget-this_cost)
        if remaining<0:
            answer=again(f"Not Enough Budget! You are missing {-1*remaining} EGP, Do you want to add this amount? Y/N")
            if not answer=="done":
                if not answer:
                    answer = again(f"Do you want to add a different amount? Y/N")
                    if answer=="done": return "done"
                    else:
                        if not answer:
                            if this_cost<cheapest_ticket():
                                return "done"
                            else:
                                answer = again(f"Do you want to select a different film? Y/N")
                                if answer == "done":
                                    return "done"
                                else:
                                    if answer:
                                        return "select another film"
                                    else:
                                        return "done"
                        else:
                            budget=enter_budget(current_budget)
                            if budget=="done": return "done"
                            print(f"\nYour New Budget is {budget}")
                            continue
                else:
                    budget-=remaining
                    print(f"Budget Added, Budget now is {budget}")
                    return budget
            else:
                return "done"
        else:
            return budget

#Returns (tickets, index) or Done
def collect_the_data(index):
    while True:
        chosen_film, chosen_film_seats, available_seats, price = variables(available_films, index)
        show_seating_chart(chosen_film, chosen_film_seats)
        tickets = pick_tickets_available_seats(chosen_film, available_seats)
        if tickets == "done":
            return "done"
        elif tickets == "select another film":
            print("\nHere's what's playing today: \n")
            list_available_films(available_films)
            index = pick_a_film(available_films)
            if index=="done": return "done"
            continue
        else:
            return index, tickets


#MAIN CODE
def main(current_budget, total_cost, index, available_films):
    while True:
        if current_budget=="done": return total_cost, current_budget, "done"
        if index =="done": return total_cost, current_budget, "done"
        data = collect_the_data(index)
        if data == "done": return total_cost, current_budget, "done"
        index, tickets = data
        chosen_film, chosen_film_seats, available_seats, price = variables(available_films, index)
        this_cost = tickets * price
        budget = make_budget_enough(current_budget, this_cost)
        if budget == "done": return total_cost, current_budget, "done"
        if budget == "select another film": continue
        total_cost+=this_cost
        current_budget=budget-this_cost
        update_seats(chosen_film_seats, tickets, index)
        chosen_film, chosen_film_seats, available_seats, price = variables(available_films, index)
        if available_seats==0:
            sold_out_films.append(available_films[index])
            available_films.pop(index)
            print(f"\nYou have bought the last ticket for {chosen_film}, Your remining budget is {current_budget}")
            if len(sold_out_films) == len(movies):
                print("\nAll Movies Are Sold Out\n")
                return total_cost, current_budget, "soldout"
            answer=again("Do you want to buy tickets for another film? Y/N")
            if  answer== "done": return total_cost, current_budget, "done"
            else:
                if answer:
                    print("\nHere's what's playing today: \n")
                    list_available_films(available_films)
                    index = pick_a_film(available_films)
                    if index == "done": return total_cost, current_budget, "done"
                    continue
                else:
                    return total_cost, current_budget, "not_soldout"
        else:
            print(f"\nYou have bought {tickets} tickets for {chosen_film} for {this_cost} EGP, Your total cost is: {total_cost} EGP, You have {current_budget} EGP left in budget!\n")
            answer = again(f"Do you want to buy more tickets for {chosen_film}? Y/N")
            if  answer== "done": return total_cost, current_budget, "done"
            else:
                if answer:
                    if current_budget < cheapest_ticket(): #Add Make Budget Enough
                        answer = again("You don't have any budget left, Do you want to add more budget? Y/N")
                        if answer=="done": return total_cost, current_budget, "done"
                        else:
                            if answer:
                                budget = make_budget_enough(enter_budget(current_budget))
                                current_budget= budget
                                if current_budget=="done": return total_cost, current_budget, "done"
                                continue
                            else:
                                return total_cost, current_budget, "done"
                    else:
                        continue
                else:
                    answer = again(f"\nDo you want to buy tickets for another film? Y/N")
                    if answer == "done": return total_cost, current_budget, "done"
                    else:
                        if answer:
                            if current_budget < cheapest_ticket():
                                answer = again("You don't have any budget left, Do you want to add more budget? Y/N")
                                if answer == "done": return total_cost, current_budget, "done"
                                else:
                                    if answer:
                                        budget = make_budget_enough(enter_budget(current_budget))
                                        if budget=="done": return total_cost, current_budget, "done"
                                        current_budget = budget
                                        print("\nHere's what's playing today: \n")
                                        list_available_films(available_films)
                                        index = pick_a_film(available_films)
                                        if index == "done": return total_cost, current_budget, "done"
                                        continue
                                    else:
                                        return total_cost, current_budget, "done"
                            else:
                                print("\nHere's what's playing today: \n")
                                list_available_films(available_films)
                                index = pick_a_film(available_films)
                                if index == "done": return total_cost, current_budget, "done"
                                continue
                        else:
                            return total_cost, current_budget, "not_soldout"

#prints the final list of films and the final cost
def final_statement(total_cost, current_budget):
    if total_cost==0:
        print("You Have Not Bought Any Tickets!")
        return "done"
    count=0
    final_cost=0
    print("\n*** Here are the movies you have purchased tickets for: *** \n")
    for index in range(len(available_films)):
        chosen_film, chosen_film_seats, available_seats, price = variables(available_films, index)
        if available_seats<len(available_films[index][2]):
            count+=1
            cost=(len(available_films[index][2])-available_seats)*price
            final_cost+=cost
            print(str(count)+f"-{chosen_film} - {10-available_seats} tickets - {cost} EGP" )
        else:
            continue

    if len(sold_out_films)>0:
        for index in range(len(sold_out_films)):
            chosen_film, chosen_film_seats, available_seats, price = variables(sold_out_films, index)
            count += 1
            cost = len(sold_out_films[index][2]) * price
            final_cost += cost
            print(str(count) + f"-{chosen_film} - {len(sold_out_films[index][2])} tickets - {cost} EGP")

    print(f"\nTotal Cost= {final_cost} EGP")
    print(f"Remaining Budget= {current_budget} EGP")


def execute(available_films):
    print("\nWelcome To Our Movie Theatre!\n")
    current_budget = make_budget_enough(enter_budget())
    total_cost = 0
    while True:
        if current_budget == "done":
            final_statement(total_cost, current_budget)
            print("Goodbye!")
            break
        print("\nToday's Program: \n")
        list_available_films(available_films)
        index = pick_a_film(available_films)
        if index == "done":
            final_statement(total_cost, current_budget)
            print("\nGoodbye!")
            break
        while True:
            outcome = main(current_budget, total_cost, index, available_films)
            total_cost, current_budget, status=outcome
            if status == "done":
                index = before_quitting()
                if index == "done":
                    final_statement(total_cost, current_budget)
                    return "GoodBye! Visit us again"
                else:
                    available_films = most_available_seats_films()
            else:
                total_cost, current_budget, status=outcome
                if status=="soldout":
                    final_statement(total_cost, current_budget)
                    return "\nPlease come again another time!\n"
                else:
                    total_cost, current_budget, status = outcome
                    return final_statement(total_cost, current_budget)

print(execute(available_films))

# # ------------------------------------------------------------
# # 2️⃣ Ask user for their available budget (must be positive number).
# # print("Please Select One of the following movies by name or number!\n")
# # ------------------------------------------------------------

# ------------------------------------------------------------
# 3️⃣ Ask which movie they want to watch.
#    - Accept number or name.
#    - Validate input.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 4️⃣ Display seating chart (10 seats, "O" = Open, "X" = Booked)
#    Example:
#    Seats: O O X O O O O X O O
# ------------------------------------------------------------


# ------------------------------------------------------------
# 5️⃣ Ask how many tickets the user wants.
#    - Ensure enough seats are available.
#    - Check if user has enough money.
# ------------------------------------------------------------



# ------------------------------------------------------------
# 6️⃣ If everything valid:
#    - Book the seats (change "O" → "X")
#    - Deduct money
#    - Confirm purchase
# ------------------------------------------------------------

# ------------------------------------------------------------
# 7️⃣ Keep looping:
#    - Let user buy tickets for another movie or quit ("done")
# ------------------------------------------------------------

# ------------------------------------------------------------
# 8️⃣ At the end:
#    - Show summary:
#      - All movies booked
#      - How much money spent
#      - Remaining budget
# ------------------------------------------------------------

# 💥 Bonus Challenge:
# - Add a function that finds the movie with the *most available seats*.
# - Suggest it to the user before they quit.
# ------------------------------------------------------------











