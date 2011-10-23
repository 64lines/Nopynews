#!/usr/bin/env python
##############################################
# Author: Julian Alexander Murillo
##############################################
# Lexinerus (GitHub)
##############################################
# Application: Nopynews
# Notify Python News
# This application show feeds in notifications
# from your favorite news sources
##############################################
# Date: 22-Oct-2011
##############################################
import feedparser
import os
import sys
import settings
import config
import time
import urllib
from subprocess import Popen, PIPE

class Nopynews:
	__source = settings.FEED_SOURCE
	
	# List of all tweets with specified word on
	# settings file.
	def news_list(self):
		lst_news = []
		
		for news in self.__source:
			feed = feedparser.parse(news)
			lst_news += feed.entries
		
		return lst_news

	# Show all news on notifications.
	def show_news(self, news_list):
		for entry in news_list:
			title = entry.title
			description = entry.description
			self.show_news_notification(title, description)
			time.sleep(settings.SECONDS_BETWEEN_NEWS)

	# Show news into a notification
	def show_news_notification(self, title, description):
		args = [title, description]
		command = ExternalApp()
		command.executeCommand(config.NOTIFY_APP, args)

class ExternalApp:
	def executeCommand(self, command, args):
		return Popen([command] + args, stdin=PIPE, stdout=PIPE)

if __name__ == '__main__':
	nopynews = Nopynews()
	lst_news = nopynews.news_list()
	nopynews.show_news(lst_news)

