from django.db import migrations


def normalize_tag_names(apps, schema_editor):
    Tag = apps.get_model("blog", "Tag")

    for tag in Tag.objects.all():
        lower_name = tag.name.lower()
        if lower_name == tag.name:
            continue

        # Check if a lowercase version already exists
        try:
            existing = Tag.objects.get(name=lower_name)
        except Tag.DoesNotExist:
            # No conflict — just rename
            tag.name = lower_name
            tag.save()
            continue

        # Duplicate exists: reassign posts from this tag to the existing one
        for post in tag.post_set.all():
            post.tags.add(existing)
            post.tags.remove(tag)
        tag.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_meta_description"),
    ]

    operations = [
        migrations.RunPython(normalize_tag_names, migrations.RunPython.noop),
    ]
