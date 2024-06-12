# tinymce_config.py

from .tinymce_templates import TINYMCE_TEMPLATES

TINYMCE_DEFAULT_CONFIG = {
    'valid_elements': '*[*]',
    'valid_children': '+body[style]',
    'extended_valid_elements': '*[*]',
    'content_css': 'css/bootstrap.min.css',
    'height': 360,
    'width': 1120,
    'image_advtab': True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'plugins': '''
        textcolor save link image media preview codesample contextmenu
        table code lists fullscreen insertdatetime nonbreaking
        directionality searchreplace wordcount visualblocks
        visualchars code fullscreen autolink charmap print hr anchor
        pagebreak template
    ''',
    'toolbar1': '''
        fullscreen preview bold italic underline | fontselect | fontsizeselect
        | forecolor backcolor | alignleft alignright aligncenter alignjustify
        | indent outdent | bullist numlist table | link | image media | codesample
    ''',
    'toolbar2': '''
        visualblocks visualchars | charmap hr | pagebreak nonbreaking 
        | code template | Heading 2 Heading 3 Heading 4 Heading 5 Heading 6
    ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'templates': TINYMCE_TEMPLATES,
}
