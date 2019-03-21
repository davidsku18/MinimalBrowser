import placeholderImageVideo

def test_placeholderImageVideo():
    assert placeholderImageVideo.placeholderImageVideo("sample_placeholderImageVideo.htm") == """<!DOCTYPE html>
<html lang="en-US">
<head>

<p>IMAGE PLACEHOLDER</p>

<p>IMAGE PLACEHOLDER</p></a>

<div class="sidesection" id="moreAboutSubject">

<p>IMAGE PLACEHOLDER</p></a>
</div>
<br><br>
</div>

<p>VIDEO PLACEHOLDER</p>

</body>
</html>"""
