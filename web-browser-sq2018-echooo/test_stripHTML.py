import pytest
import stripHTML

def test_stripHTML1():
    assert stripHTML.stripHTML("<html><body>hi<div>Hello</div></body></html>") == "hiHello"
    
def test_stripHTML2():
    assert stripHTML.stripHTML('<body>hi<div>World</div><script>helloworld</script><script crossorigin="anonymous" integrity="sha512-jqvDaL8uGENbC1rsifCdxmfE5RQmxtizkQ1xMGfvpSbwdKnG1vYz/z/BKuMEtJxU7/cY0IFKZlpgmUrMPtu4oQ==" src="https://assets-cdn.github.com/assets/frameworks-8eabc368bf2e.js" type="application/javascript"></script></body>') == "hiWorld"
    
def test_stripHTML3():
    assert stripHTML.stripHTML("<html><body><h1>Hello</h1>World<!--asdf--></body></html>") == "HelloWorld"

#def test_stripHTML4():
    #assert stripHTML.stripHTML("<body><script>!function(e,n,t){var o,c=e.getElementsByTagName(n)[0];e.getElementById(t)||((o=e.createElement(n)).id=t,o.src=\"//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5\",c.parentNode.insertBefore(o,c))}(document,\"script\",\"facebook-jssdk\");</script>hi</body>") == "hi"
