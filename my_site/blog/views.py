from django.shortcuts import render
from datetime import date


all_posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Someone",
    "date": date(2025, 7, 12),
    "title": "Mountain hiking",
    "excerpt": "Amazing view",
    "content": """"
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?
    """

  },
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Someone",
    "date": date(2025, 6, 12),
    "title": "Mountain hiking",
    "excerpt": "Amazing view",
    "content": """"
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?
    """

  },
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Someone",
    "date": date(2025, 5, 12),
    "title": "Mountain hiking",
    "excerpt": "Amazing view",
    "content": """"
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis dignissimos atque quae cumque vitae
        exercitationem esse, minima error, nisi odio, minus laboriosam aut. Ducimus nisi, pariatur inventore
        necessitatibus sint rerum?
    """

  }
]

def get_date(post):
  return post['date']

# Create your views here.
def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", { "posts": latest_posts })

def posts(request):
  return render(request, "blog/all-posts.html")

def post_details(request, slug):
  return render(request, "blog/post-detail.html")
