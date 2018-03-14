from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.db.models import Count

from gallery.models import Group, Submission, GalleryProfile
 
class FrontPage(TemplateView):
    template_name = 'gallery/index.html'
     
    def get_context_data(self, **kwargs):
        return super().get_context_data(
            groups=self.__get_top_groups(),
            submissions=self.__get_recent_submissions(),
            **kwargs
        )

    def __get_top_groups(self):
        return Group.objects.annotate(userCount=Count('groupmembership')).order_by('-userCount')[:10]

    def __get_recent_submissions(self):
        prefs = GalleryProfile.get_prefs(self.request.user)
        submissions = Submission.objects.filter(is_visible=True)
        if not prefs['show_nsfw']:
            submissions = submissions.filter(is_nsfw=False)

        return submissions[:10]


class UserPage(DetailView):
    template_name = 'gallery/userpage.html'
    
    def get_queryset(self):
        return get_user_model().objects.filter(is_active=True)
    
    def get_context_object_name(self, obj):
        # 'user' context variable is already used
        return None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        tab = self.request.GET.get('tab', 'drawings')

        if tab == 'favorites':
            submissions = ctx['object'].favorite_submission_set.filter(is_visible=True)

        else:
            submissions = ctx['object'].submission_set.all()
            if self.request.user != ctx['object']:
                prefs = GalleryProfile.get_prefs(self.request.user)

                submissions = submissions.filter(is_visible=True)
                if not prefs['show_nsfw']:
                    submissions = submissions.filter(is_nsfw=False)
                
        
        paginator = Paginator(submissions, 10)
        ctx.update({
            'paginator': paginator,
            'page_obj': paginator.page(self.request.GET.get('page', 1)),
            'tab': tab,
            })

        return ctx
