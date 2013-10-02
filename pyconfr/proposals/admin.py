from django.contrib import admin

from pyconfr.proposals.models import TalkProposal, TutorialProposal, PosterProposal


class ProposalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'speaker'
    )


admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
admin.site.register(PosterProposal, ProposalAdmin)
