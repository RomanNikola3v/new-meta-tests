
class GqlValid:

    def __init__(self):
        self.news = {'fields': [{'name': 'source', 'type': {'kind': 'OBJECT', 'name': 'Source'}},
            {'name': 'exclusive', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'day_news', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'has_picture', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'has_video', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'bookmaker',
             'type': {'kind': 'OBJECT', 'name': 'Bookmaker'}},
            {'name': 'id', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'slug', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'name', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'published', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'publication_date',
             'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'preview', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'annonce', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'content', 'type': {'kind': 'SCALAR', 'name': 'Editor'}},
            {'name': 'rating', 'type': {'kind': 'SCALAR', 'name': 'Float'}},
            {'name': 'microData', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'author', 'type': {'kind': 'OBJECT', 'name': 'Author'}},
            {'name': 'categories', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'main_category',
             'type': {'kind': 'OBJECT', 'name': 'Category'}},
            {'name': 'tags', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'related', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'url', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'edit_url', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'h1', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'title', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'description', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'hreflang', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'breadcrumbs', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'created_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'updated_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'comments_count',
             'type': {'kind': 'SCALAR', 'name': 'Int'}},
            {'name': 'comments',
             'type': {'kind': 'OBJECT', 'name': 'CommentPaginator'}}],
 'name': 'News'}
        self.bonus = {'fields': [{'name': 'id', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'slug', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'name', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'published', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'publication_date',
             'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'publication_end_date',
             'type': {'kind': 'SCALAR', 'name': 'DateTime'}},
            {'name': 'start_date', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'end_date',
             'type': {'kind': 'SCALAR', 'name': 'DateTime'}},
            {'name': 'expired', 'type': {'kind': 'SCALAR', 'name': 'Boolean'}},
            {'name': 'preview', 'type': {'kind': 'OBJECT', 'name': 'Image'}},
            {'name': 'annonce', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'before_content',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'content', 'type': {'kind': 'SCALAR', 'name': 'Editor'}},
            {'name': 'properties', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'exclusive',
             'type': {'kind': 'SCALAR', 'name': 'Boolean'}},
            {'name': 'verified', 'type': {'kind': 'SCALAR', 'name': 'Boolean'}},
            {'name': 'bonus_text',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'button_text',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'bonus', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'bonus_rub', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'currency', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'spider_data',
             'type': {'kind': 'SCALAR', 'name': 'SpiderData'}},
            {'name': 'pluses', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'minuses', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'promo_code',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'microData', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'microDataForListItems',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'hreflang', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'rating', 'type': {'kind': 'SCALAR', 'name': 'Float'}},
            {'name': 'author', 'type': {'kind': 'OBJECT', 'name': 'Author'}},
            {'name': 'tags', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'bookmaker',
             'type': {'kind': 'OBJECT', 'name': 'Bookmaker'}},
            {'name': 'promo', 'type': {'kind': 'OBJECT', 'name': 'PromoLink'}},
            {'name': 'url', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'edit_url', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'h1', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'title', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'description', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'breadcrumbs', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'created_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'updated_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'updated_at_public',
             'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'comments_count',
             'type': {'kind': 'SCALAR', 'name': 'Int'}},
            {'name': 'comments',
             'type': {'kind': 'OBJECT', 'name': 'CommentPaginator'}}],
 'name': 'Bonus'}
        self.tips = {'fields': [{'name': 'preview_text',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'team_home', 'type': {'kind': 'OBJECT', 'name': 'Team'}},
            {'name': 'team_away', 'type': {'kind': 'OBJECT', 'name': 'Team'}},
            {'name': 'start_date',
             'type': {'kind': 'SCALAR', 'name': 'DateTime'}},
            {'name': 'end_date',
             'type': {'kind': 'SCALAR', 'name': 'DateTime'}},
            {'name': 'coefficient',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'bets', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'bookmakers', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'top', 'type': {'kind': 'SCALAR', 'name': 'Boolean'}},
            {'name': 'id', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'slug', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'name', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'preview_name',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'published', 'type': {'kind': 'NON_NULL', 'name': None}},
                                {'name': 'show_bets',
                                 'type': {'kind': 'SCALAR',
                                              'name': 'Boolean'}},

                                {'name': 'publication_date',
             'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'preview', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'annonce', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'content', 'type': {'kind': 'SCALAR', 'name': 'Editor'}},
            {'name': 'rating', 'type': {'kind': 'SCALAR', 'name': 'Float'}},
            {'name': 'microData', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'microDataPreview',
             'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'author', 'type': {'kind': 'OBJECT', 'name': 'Author'}},
            {'name': 'categories', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'main_category',
             'type': {'kind': 'OBJECT', 'name': 'Category'}},
            {'name': 'tags', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'event', 'type': {'kind': 'OBJECT', 'name': 'Event'}},
            {'name': 'related', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'highlight', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'url', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'edit_url', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'h1', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'title', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'description', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'hreflang', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'breadcrumbs', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'created_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'updated_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'comments_count',
             'type': {'kind': 'SCALAR', 'name': 'Int'}},
            {'name': 'votes', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'comments',
             'type': {'kind': 'OBJECT', 'name': 'CommentPaginator'}}],
 'name': 'Tips'}
        self.article = {'fields': [{'name': 'type', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'id', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'slug', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'name', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'published', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'publication_date',
             'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'preview', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'annonce', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'content', 'type': {'kind': 'SCALAR', 'name': 'Editor'}},
            {'name': 'rating', 'type': {'kind': 'SCALAR', 'name': 'Float'}},
            {'name': 'microData', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'hreflang', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'author', 'type': {'kind': 'OBJECT', 'name': 'Author'}},
            {'name': 'categories', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'main_category',
             'type': {'kind': 'OBJECT', 'name': 'Category'}},
            {'name': 'tags', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'related', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'bonusBookmaker',
             'type': {'kind': 'OBJECT', 'name': 'Bookmaker'}},
            {'name': 'tips', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'url', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'edit_url', 'type': {'kind': 'SCALAR', 'name': 'String'}},
            {'name': 'h1', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'title', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'description', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'breadcrumbs', 'type': {'kind': 'LIST', 'name': None}},
            {'name': 'created_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'updated_at', 'type': {'kind': 'NON_NULL', 'name': None}},
            {'name': 'comments_count',
             'type': {'kind': 'SCALAR', 'name': 'Int'}},
            {'name': 'comments',
             'type': {'kind': 'OBJECT', 'name': 'CommentPaginator'}}],
 'name': 'Article'}