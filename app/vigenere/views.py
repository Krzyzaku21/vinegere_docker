from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import EncryptVigenere, DecryptVigenere
from .code import keyrep, cipher_encryption, cipher_decryption
from .forms import EncryptVigenereForm, DecryptVigenereForm
from . import code


def score(request, pk):
    scored = get_object_or_404(EncryptVigenere, pk=pk)
    return render(request, 'score.html', {'scored': scored})


def score2(request, pk):
    descored = get_object_or_404(DecryptVigenere, pk=pk)
    return render(request, 'score2.html', {'descored': descored})


def encrypter(request):
    if request.method == "POST":
        form = EncryptVigenereForm(request.POST)
        if form.is_valid():
            scored = form.save(commit=False)
            move_key = keyrep(form.cleaned_data['plain_text'], form.cleaned_data['plain_key'])
            encrypt = cipher_encryption(form.cleaned_data['plain_text'], move_key)
            scored.plain_text = encrypt
            scored.plain_key = move_key
            scored.save()
            return redirect('score', pk=scored.pk)
    else:
        form = EncryptVigenereForm()
    context = {
        'form': form,
    }
    return render(request, 'encrypter.html', context)


def decrypter(request, pk):
    de_form = EncryptVigenere.objects.get(pk=pk)
    text = getattr(de_form, 'plain_text')
    key = getattr(de_form, 'plain_key')
    form = DecryptVigenereForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            base_key = form.cleaned_data['plain_key']
            descored = form.save(commit=False)
            if base_key == key:
                decrypt = cipher_decryption(text, base_key)
                descored.encrypt_text = decrypt
                descored.save()
                return redirect('score2', pk=descored.pk)
    else:
        form = DecryptVigenereForm()
    context = {
        'key': key,
        'text': text,
        'form': form,
    }
    return render(request, 'decrypter.html', context)
