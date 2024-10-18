PREFIX = /usr/local

bible: bible.sh bible.awk bible.tsv
	cat bible.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar czf - bible.awk bible.tsv >> $@
	chmod +x $@

test: bible.sh
	shellcheck -s sh bible.sh

clean:
	rm -f bible

install: bible
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f bible $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/bible

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/bible

.PHONY: test clean install uninstall
