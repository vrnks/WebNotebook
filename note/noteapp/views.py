from .forms import TagForm, NoteForm
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *

def main(request):
    notes = Note.objects.all()
    return render(request, 'noteapp/index.html', {"notes": notes})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/add_tag.html', {'form': form})

    return render(request, 'noteapp/add_tag.html', {'form': TagForm()})

def add_note(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/add_note.html', {"tags": tags, 'form': form})

    return render(request, 'noteapp/add_note.html', {"tags": tags, 'form': NoteForm()})

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'noteapp/detail.html', {"note": note})

def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect(to='noteapp:main')

# # Додавання функціоналу пошуку
# def search_notes(request):
#     query = request.GET.get('query', '')
#     notes = Note.objects.filter(name__icontains=query)
#     return render(request, 'notebook/search_results.html', {"notes": notes, "query": query})

def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    all_tags = Tag.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            edited_note = form.save(commit=False)
            edited_note.tags.clear()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                edited_note.tags.add(tag)
            edited_note.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/edit_note.html', {"note": note, 'form': form, 'all_tags': all_tags})
    else:
        form = NoteForm(instance=note)
        return render(request, 'noteapp/edit_note.html', {"note": note, 'form': form, 'all_tags': all_tags})

def search_and_sort_notes(request):
    query = request.GET.get('query', '')
    tag_name = request.GET.get('tag', '')

    notes = Note.objects.filter(name__icontains=query)
    if tag_name:
        notes = notes.filter(tags__name=tag_name)

    all_tags = Tag.objects.all()

    return render(request, 'noteapp/index.html', {"notes": notes, "all_tags": all_tags, "query": query, "tag_name": tag_name})
