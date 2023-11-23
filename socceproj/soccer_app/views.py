from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your models here.
def say_hello(request):
    
    return HttpResponse("<h1>Hello, World !</h1>")

def say_hellohtml(request):
    params={"names":['John','Mary','Peter','Andy','Tom']}
    
    return render(request, 'hello.html', params)
# Create your views here.


# list all players from database
def list_players(request):
    # get all players from database
    with connection.cursor() as cursor:
        # execute the query
        cursor.execute("SELECT * FROM player")
        
        # recieve the results
        players = cursor.fetchall()
    # pass the params to the template
    return render(request, 'list-players.html', {'players': players})

def add_player(request):
    if request.method=="POST":
       
       # get the post object
       post=request.POST
       
       # read each field from the post object
       player_id = post['player_id']
       player_fname = post['first_name']
       player_lname = post['last_name']
       player_postition = post['position']
       
       # createa a connection pass the query string
       with connection.cursor() as cursor:
           # execute the query
           cursor.execute("INSERT INTO player VALUES (%s, %s, %s, %s)", [int(player_id), player_fname, player_lname, player_postition])
           
    return render(request, 'add-players.html')

# def update player view function
def update_player(request):
    if request.method=="POST":
     
       # get the post object
       post=request.POST
       
       # read each field from the post object
       player_id = post['player_id']
       player_fname = post['first_name']
       player_lname = post['last_name']
       player_postition = post['position']
        
       with connection.cursor() as cursor:
            # execute the query
            cursor.execute("UPDATE player SET FirstName=%s, LastName=%s, position=%s WHERE PlayerID=%s", [player_fname, player_lname, player_postition, int(player_id)])
        
    return render(request, 'edit-player.html')

# creae a delete player function
def delete_player(request):
    if request.method=="POST":
        # get the post object
        post=request.POST
        # read the player id
        player_id = post['player_id']
        player_lname = post['last_name']
        
        if player_id != '':
            # create a connection
            with connection.cursor() as cursor:
                # execute the query
                cursor.execute("DELETE FROM player WHERE PlayerID=%s", [int(player_id)])
                
        elif player_lname != '':
            # create a connection
            with connection.cursor() as cursor:
                # execute the query
                cursor.execute("DELETE FROM player WHERE LastName=%s", [player_lname])

    return render(request, 'delete-player.html')