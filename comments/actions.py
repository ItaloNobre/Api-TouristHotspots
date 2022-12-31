def disapprove_comments(modeladmin, request, queryset):
    queryset.update(okay = False)

def approved_comments(modeladmin, request, queryset):
    queryset.update(okay = True)

disapprove_comments.short_description = "Reprovar Comentarios"
approved_comments.short_description = "Aprovar comentatios"