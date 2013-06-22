# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Request Handler for /foursquare_test endpoint."""

__author__ = 'me@destil.cz (David Vavra)'

import logging
import webapp2
import foursquare


class FoursquareHandler(webapp2.RequestHandler):
  """Request Handler for foursquare test."""

  def get(self):
    """Handles all gets."""
    client = foursquare.Foursquare(client_id='3XRAA220QQWY4XHJH11TGRGEFYSW03YOBUL3225Y3KBMJ3XY', client_secret='4WYHXNQQVUYSTJGFMQZNRFBUKU4GFKPEBKFM0HFBVD42HN5U')
    logging.info(client.venues('40a55d80f964a52020f31ee3'))
    

FOURSQUARE_ROUTES = [
    ('/foursquaretest', FoursquareHandler)
]
