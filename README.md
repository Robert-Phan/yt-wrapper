# yt-wrapper <!-- omit in toc -->
**A simple wrapper around the Youtube Data API.**
***

**Table of contents**
- [Introduction](#introduction)
- [Tutorial/Quickstart](#tutorialquickstart)
- [Guides](#guides)
- [API Reference](#api-reference)
  - [`Client`](#client)
  - [Methods](#methods)
    - [`Playlist`](#playlist)
    - [`PlaylistItem`](#playlistitem)
    - [`Thumbnail`](#thumbnail)
    - [`Comment`](#comment)
    - [`CommentThread`](#commentthread)
    - [`I18n`](#i18n)
    - [`VideoCategory`](#videocategory)
    - [`VideoAbuseReportReason`](#videoabusereportreason)
    - [`Video`](#video)
    - [`Channel`](#channel)
    - [`ChannelSection`](#channelsection)
    - [`Search`](#search)
    - [`Subscription`](#subscription)
  - [Resources](#resources)
    - [`PlaylistResource`](#playlistresource)
    - [`PlaylistListResponse`](#playlistlistresponse)

## Introduction
The goal of this project is to create an (almost) complete, comprehensive Python wrapper for the Youtube Data API. 

**WARNING:** *This project is still unfinished. Breaking changes can be made at any time. Usse at your own risk.*

**NOTE:** This project is my first ever attempt at creating a semi-decent Python package.
## Tutorial/Quickstart 

This section will demonstrate a simple program written using this package. We will be retrieving a video's title with it's ID.

For the full documentation for this package, see the [API Reference](#api-reference).  

1. **Package installation** 
   
    To use this package, you must have `Python 3.10` or higher.

    Install using `pip`:
    ```
    pip install yt-wrapper
    ```
    It is recommended that you use a virtual environment when installing this package.

2. **Authorization**

    *TODO: write the authorizaton process.*

3. **Using the API**
    
    - Setting up the client  

        ```python
        from ytwrapper.client import Client
        youtube = Client.from_client_secrets(path_to_client_secrets_file, scopes=['https://www.googleapis.com/auth/youtube.readonly'])
        ```
    - Getting the video

        ```python
        video = youtube.video.list(
            part='snippet',        # the `snippet` part, which contains the video titles
            id='dQw4w9WgXcQ'       # the Video id of the video we're retrieving
        )

        print(video.snippet.title) # Output: 'Rick Astley - Never Gonna Give You Up (Official Music Video)'
        ```

## Guides

## API Reference

### `Client`
The `Client` class represents a Youtube client, containing the entire API of this project.

**Methods:**
- `from_client_secrets` 
    
    Creates a new `Client` object from an OAuth2 [Installed App](https://developers.google.com/youtube/v3/guides/auth/installed-apps) client secrets file. Will prompt the user to go to a link and give access, where the user will have to copy a code given at the end to the terminal.
    - `client_secrets_file: str`
        
        The path to the client secrets JSON file. This file should contain the client secrets of an [Installed App project.](https://developers.google.com/youtube/v3/guides/auth/installed-apps)
    - `scopes: list[str]`

        [The scope of the program](https://developers.google.com/youtube/v3/guides/auth/installed-apps#identify-access-scopes), specifying the permissions the user must give. Each method in the API has it's own scopes that it needs for it to be used.
    - `token_store: str = "token.pickle"`

        The path to the file used to store the OAuth2 access and refresh token.

**Attributes:**
- `playlist`: The interface for [Playlist](#playlist).
- `playlist_item`: The interface for [PlaylistItem](#playlistitem).
- `thumbnail`: The interface for [Thumbnail](#thumbnail).
- `comment`: The interface for [Comment](#comment).
- `comment_thread`: The interface for [CommentThread](#commentthread).
- `i18n`: The interface for [I18n](#i18n).
- `video_category`: The interface for [VideoCategory](#videocategry).
- `video_abuse_report_reason`: The interface for [VideoAbuseReportReason](#videoabusereportreason).
- `video`: The interface for [Video](#video).
- `channel`: The interface for [Channel](#channel).
- `channel_section`: The interface for [ChannelSection](#channelsection).
- `search`: The interface for [Search](#search).
- `subscription`: The interface for [Subscription](#subscription).

***
### Methods

This section describes the methods available in the API. These methods are accessible via the [`Client`](#client) object.
#### `Playlist`
**Methods:**
- <details> <summary><code>list</code></summary> 

    Returns a collection of playlists.  
    **Required** parameters:
    - `part: PlaylistPartType` 
  
        `part` specifies what properties will be returned by the request.  
        Valid values include:
        - 'content_details'
        - 'localizations'
        - 'player'
        - 'snippet'
        - 'status'

    **Filters** (specify exactly one):
    - `id: list[str]|str` 

        The playlist ID/list of playlist IDs that will be returned.
    - `channel_id: str` 

        Specifies a channel ID whose playlists will be returned.
    - `mine: bool`

        Specifies that the API should retrieve the playlists of the authorised user.
    
    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.

    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/list)
</details>

- <details> <summary><code>insert</code></summary> 

    Creates a playlist.  
    **Required** parameters:
    - `body: PlaylistResource`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.  
        **Values you are able to set**:
        - `snippet.title` (Required)
        - `snippet.description`
        - `snippet.privacy_status`
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `on_behalf_of_content_owner: str`

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/insert)
</details>

- <details> <summary><code>update</code></summary> 

    Updates a playlist.  
    **Required** parameters:
    - `body: PlaylistResource`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.  
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `on_behalf_of_content_owner: str`

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/update)
</details>

- <details> <summary><code>delete</code></summary> 

    Deletes a playlist.  
    **Required** parameters:
    - `playlist_id: str`

        The ID of the Playlist that will be deleted.
    - `on_behalf_of_content_owner: str`

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/delete)
</details>

#### `PlaylistItem`
#### `Thumbnail`
#### `Comment`
#### `CommentThread`
#### `I18n`
#### `VideoCategory`
#### `VideoAbuseReportReason`
#### `Video`
#### `Channel`
#### `ChannelSection`
#### `Search`
#### `Subscription`

### Resources

This section describes the resources and responses used in the API. These classes are most often used in responses, as well as in methods that require a request body.  
Note that the attributes of these resources are in `snake_case`, not `camelCase` like in the original response. This is so as to follow the Python conventions.  
Also note that each resource has a `to_dict` method that returns the original response. That original response is a Python dictionary, and it's keys *will* be in `camelCase`. 
#### `PlaylistResource`

Represents a Youtube playlist resource. [More information available at Google's official documentation.](https://developers.google.com/youtube/v3/docs/playlists)
#### `PlaylistListResponse`

The returned response of the [`Playlist`](#playlist) `list` method. [More information available at Google's official documentation.](https://developers.google.com/youtube/v3/docs/playlists/list#response)
