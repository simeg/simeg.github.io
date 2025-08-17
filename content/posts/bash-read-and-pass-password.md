+++
title = "Passing passwords in Bash without storing them"
date = 2025-08-17
description = "A clever way to pass passwords in Bash scripts without exposing them in shell history"

[taxonomies]
tags = ["bash", "tech", "cli"]
+++

Today I learned something cool that I think is worth sharing. I was working on a script where I
needed to make a curl request to acquire a token, for which I needed to pass a password.

My first instinct was to put the password in the script, {% bold() %}but then I might've
accidentally pushed the script with my password in it{% end %} (I was in a git repo). So I decided
not to do that.
The next option I could think of was to pass the password as an environment variable, which is a common
practice. So I would run my script like this:

```bash
export SECRET=my_password && ./my_script.sh

# my_script.sh
password=$SECRET
```

{% bold() %}The problem with this approach is that your password will now be saved in your shell
history!{% end %} You might, like me, have a smart shell history manager
like [Atuin](http://atuin.sh/) that detects and doesn't save it to your history. But not everyone
does.

Instead, we should ask for the password and pass it to the script without exposing it in any way.

```bash
( printf 'Password? ' >/dev/tty; IFS= read -rs pass </dev/tty; printf '\n' >/dev/tty; MY_PASSWORD="$pass" exec ./my_script.sh )

# my_script.sh
password=$MY_PASSWORD
```

So what's happening here?
* Subshell `(...)`: Runs in its own shell; {% bold() %}variables die when it exits—no unset needed.{% end %}
* `printf 'Password: ' >/dev/tty`: Prints a prompt to the terminal, not stdout, so it doesn't interfere with the script's output.
* `IFS=`: Disables trimming/splitting so leading/trailing spaces in the password aren't lost.
* `read -rs pass </dev/tty`: Reads from the terminal into `pass`
  * `-r` don't treat backslashes specially.
  * `-s` silent (no echo) so the password isn't shown.
* `printf '\n' >/dev/tty`: add a newline because `-s` suppressed it, so that the next prompt starts on a new line.
* `MYAPP_PASSWORD="$pass"`: Sets an env var only for that command; avoids a global export.
* `exec`: Replaces the subshell with your script (no extra process, nothing runs after). Optional; `./my_script.sh` also works.
{% end %}

This obviously only works for manually executed scripts and not scheduled ones. I've never seen this
before and thought it was pretty clever so I wanted to share.
