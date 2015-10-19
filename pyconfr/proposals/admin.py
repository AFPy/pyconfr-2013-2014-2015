from django.contrib import admin

from pyconfr.proposals.models import TalkProposal, TutorialProposal, PosterProposal, SprintProposal


class ProposalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'speaker',
        'audience_level',
    )


admin.site.register(TalkProposal, ProposalAdmin)
admin.site.register(TutorialProposal)
admin.site.register(PosterProposal, ProposalAdmin)
admin.site.register(SprintProposal)
