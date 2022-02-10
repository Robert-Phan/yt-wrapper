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
    - [`PlaylistItemResource`](#playlistitemresource)
    - [`ThumbnailResource`](#thumbnailresource)
    - [`CommentResource`](#commentresource)
    - [`CommentThreadResource`](#commentthreadresource)
    - [`I18nResource`](#i18nresource)
    - [`VideoCategoryResource`](#videocategoryresource)
    - [`VideoAbuseReportReasonResource`](#videoabusereportreasonresource)
    - [`VideoResource`](#videoresource)
    - [`ChannelResource`](#channelresource)
    - [`ChannelSectionResource`](#channelsectionresource)
    - [`SearchResult`](#searchresult)
    - [`SubscriptionResource`](#subscriptionresource)

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
<!-- TODO: Add in return types for each of these. -->
This section describes the methods available in the API. These methods are accessible via the [`Client`](#client) object.

<!--m-start Playlist -->
#### `Playlist`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a collection of playlists.  
    **Required** parameters:
    - `part: PlaylistPartType`

        Specifies what properties will be returned by the request.

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

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Creates a playlist.  
    **Required** parameters:
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: [PlaylistResource](#playlistresource)`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.
        **Values you are able to set**:
        - `snippet.title` (Required)
        - `snippet.description`
        - `snippet.privacy_status`

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`[PlaylistResource](#playlistresource)`](#[playlistresource](#playlistresource))

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a playlist.  
    **Required** parameters:
    - `part: PlaylistPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: PlaylistResource`

        The [`PlaylistResource`](#playlistresource) which specifies the details of this playlist.
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.`

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistResource`](#playlistresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a playlist.  
    **Required** parameters:
    - `playlist_id: str`

        The ID of the playlist that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlists/delete)
</details>

<!--m-end Playlist -->
<!--m-start PlaylistItem -->
#### `PlaylistItem`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a collection of playlist items that match the API request parameters.  
    **Required** parameters:
    - `part: PlaylistItemPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: list[str]|str`

        The ID/list of IDs of the playlist items that should be returned.
    - `playlist_id: str`

        The ID of the playlist whose videos will be retrieved.

    **Optional** parameters:
    - `video_id: str`

        Specifies that the request should return only the playlist items that contain the specified video.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playliststems/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Modifies a playlist item.  
    **Required** parameters:
    - `part: PlaylistItemPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: PlaylistItemResource`

        The [`PlaylistItemResource`](#playlistitemresource) which specifies the details of the playlist item.
        **Values you are able to set**:
        - `id` (Required)
        - Otherwise, same as the above `insert` method.`

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemResource`](#playlistitemresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Inserts a video into a playlist.  
    **Required** parameters:
    - `part: PlaylistItemPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: PlaylistItemResource`

        The [`PlaylistItemResource`](#playlistitemresource) which specifies the details of the playlist item.
        **Values you are able to set**:
        - `snippet.playlist_id` (Required)
        - `snippet.resource_id` (Required)
        - `snippet.position` (Required)
        - `content_details.note` (Required)
        - `content_details.start_at` (Required)
        - `content_details.end_at` (Required)

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`PlaylistItemResource`](#playlistitemresource)

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a playlist item.  
    **Required** parameters:
    - `playlist_item_id: str`

        The ID of the playlist item that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/playlistItems/delete)
</details>

<!--m-end PlaylistItem -->
<!--m-start Thumbnail -->
#### `Thumbnail`
**Methods:**
- <details><summary><code>set</code></summary>
    <br>

    Uploads a custom video thumbnail to YouTube and sets it for a video.  
    **Required** parameters:
    - `thumbnail_file: str`

        The path to the file of the thumbnail.
    - `video_id: str`

        The ID of the video for the thumbnail.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/thumbnails/set)
</details>

<!--m-end Thumbnail -->
<!--m-start Comment -->
#### `Comment`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of comments.  
    **Required** parameters:
    - `part: CommentPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id`

        The id of the comment that should be retrived.
    - `parent_id`

        The ID of the top-level comment whose replies should be retrieved.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `text_format: Literal['html', 'plain_text']`

        The format of the returned comment.

    [Reference](https://developers.google.com/youtube/v3/docs/comments/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Create a reply to a top-level comment. To create a top-level comment, use CommentThread.insert instead.  
    **Required** parameters:
    - `part: CommentPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: CommentResource`

        The [`CommentResource`](#commentresource) which specifies the details of the reply.
        **Values you are able to set**:
        - `snippet.text_original`
        - `snippet.parent_id`

    **Returns:** [`CommentResource`](#commentresource)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Modifies a comment.  
    **Required** parameters:
    - `part: CommentPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: CommentResource`

        The [`CommentResource`](#commentresource) which specifies the details of the comment.
        **Values you are able to set**:
        - `id`
        - `snippet.text_original`

    **Returns:** [`CommentResource`](#commentresource)

    [Reference](https://developers.google.com/youtube/v3/docs/comments/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a comment.  
    **Required** parameters:
    - `comment_id: str`

        The ID of the comment that should be deleted.

    [Reference](https://developers.google.com/youtube/v3/docs/comments/delete)
</details>

<!--m-end Comment -->
<!--m-start CommentThread -->
#### `CommentThread`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of comment threads.  
    **Required** parameters:
    - `part: CommentThreadPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `id: str`

        The ID of the comment.
    - `channel_id: str`

        Specifies the API to retrieve all comment threads which contain comments from this channel.
    - `video_id: str`

        Specifies the ID of the video whose comments should be retrieved.
    - `all_threads_related_to_channel_id: str`

        Specifies the API to return all comment threads associated with the specified channel.

    **Optional** parameters:
    - `moderation_status: Literal['held_for_review', 'likely_spam', 'published']`

        Specifies that all returned comments are of the given moderation state.
    - `order: Literal['time', 'relevance']`

        Specifies the order the returned comment threads should be in.
    - `text_format: Literal['html', 'plain_text']`

        The format of the returned comment.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/commentThreads/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Create a new top-level comment.  
    **Required** parameters:
    - `part: CommentThreadPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: CommentThreadResource`

        The [`CommentThreadResource`](#commentthreadresource) which specifies the details of the comment.
        **Values you are able to set**:
        - `snippet.channel_id`
        - `snippet.video_id`
        - `snippet.top_level_comment.snippet.text_original`

    **Returns:** [`CommentThreadResource`](#commentthreadresource)

    [Reference](https://developers.google.com/youtube/v3/docs/commentThreads/insert)
</details>

<!--m-end CommentThread -->
<!--m-start I18n -->
#### `I18n`
**Methods:**
<!--m-end I18n -->
<!--m-start VideoCategory -->
#### `VideoCategory`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Returns a list of categories that can be associated with YouTube videos.  
    **Optional** parameters:
    - `id: str|list[str]`

        The ID of the video category to be retrieved.
    - `region_code: str`

        Specifies the API to retrive all video categories in the specified region code.

    [Reference](https://developers.google.com/youtube/v3/docs/videoCategories/list)
</details>

<!--m-end VideoCategory -->
<!--m-start VideoAbuseReportReason -->
#### `VideoAbuseReportReason`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of reasons that can be used to report abusive videos.  
    [Reference](https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list)
</details>

<!--m-end VideoAbuseReportReason -->
<!--m-start Video -->
#### `Video`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieves a list of videos.  
    **Required** parameters:
    - `part: VideoPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `chart: Literal['most_popular']`

        Identifies the chart that you want to retrieve.
    - `id: list[str]|str`

        Specifies the video(s) that should be retrieved.
    - `my_rating: Literal["like", "dislike"]`

        Specifies that the API should only retrieve videos that the user has disliked/like.

    **Optional** parameters:
    - `region_code: str`

        Specifies the API to select a video chart in the specified region code.
        Used in conjunction with the `chart` parameter.
    - `video_category_id: str`

        Specifies the video category for which the chart should be retrieved.
        Used in conjunction with the `chart` parameter.
    - `max_height: int`

        Specifies the maximum height of the embedded player returned in the `player.embed_html` property
    - `max_width: int`

        Specifies the maximum width of the embedded player returned in the `player.embed_html` property
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Upload a video to youtube.  
    **Required** parameters:
    - `part: VideoPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: VideoResource`

        The [`VideoResource`](#videoresource) which specifies the details of the comment.
        **Values you are able to set**:
        - `snippet.title`
        - `snippet.description`
        - `snippet.tags`
        - `snippet.category_id`
        - `snippet.default_language`
        - `status.embeddable`
        - `status.license`
        - `status.public_stats_viewable`
        - `status.publish_at`
        - `status.self_declared_made_for_kids`
        - `recording_details.recording_date`
    - `media_body: str`

        The path to the file of the uploaded video.

    **Optional** parameters:
    - `notify_subscribers: bool`

        Indicates whether YouTube should notify subscribers to the video's channel about the video.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoResource`](#videoresource)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a video's metadata.  
    **Required** parameters:
    - `part: VideoPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: VideoResource`

        The [`VideoResource`](#videoresource) which specifies the details of the video.
        **Values you are able to set**:
        - `id` (Required)
        - `snippet.title (Required IF updating the `snippet` attribute.)`
        - `snippet.description`
        - `snippet.tags`
        - `snippet.category_id`
        - `snippet.default_language`
        - `status.embeddable`
        - `status.license`
        - `status.public_stats_viewable`
        - `status.publish_at`
        - `status.self_declared_made_for_kids`
        - `recording_details.recording_date`

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`VideoResource`](#videoresource)

    [Reference](https://developers.google.com/youtube/v3/docs/videos/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a video.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/delete)
</details>

- <details><summary><code>rate</code></summary>
    <br>

    Rate a video.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video to rate.
    - `rating: Literal['dislike', 'like', 'none']`

        The rating to give to the video.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/rate)
</details>

- <details><summary><code>get_rating</code></summary>
    <br>

    Get a video's rating.  
    **Required** parameters:
    - `video_id: str`

        The ID of the Video whose rating shall be retrieved.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/videos/getrating)
</details>

<!--m-end Video -->
<!--m-start Channel -->
#### `Channel`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a channel/list of channel resources.  
    **Required** parameters:
    - `part: ChannelPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `mine: bool`

        Specifies that the API should retrieve the channel of the authorised user.
    - `for_username: str`

        Specifies the name of the channel that should retrieve.
    - `id: str|list[str]`

        The ID of the channel to be retrieved.
    - `managed_by_me: bool`

        Specifies that the API should retrieve channels managed by the authenticated user.

    **Optional** parameters:
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/channels/list)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a channel.  
    **Required** parameters:
    - `body: ChannelResource`

        The [`ChannelResource`](#channelresource) which specifies the details of the channel.
        **Values you are able to set**:
        - `branding_settings.channel.description`
        - `branding_settings.channel.country`
        - `branding_settings.channel.default_language`
        - `branding_settings.channel.keywords`
        - `branding_settings.channel.moderate_comments`
        - `branding_settings.channel.tracking_analytics_account_id`
        - `branding_settings.channel.unsubscribed_trailer`
        - `status.self_declared_made_for_kids`
    - `part: ChannelPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelResource`](#channelresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channels/update)
</details>

<!--m-end Channel -->
<!--m-start ChannelSection -->
#### `ChannelSection`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve a list of channel sections.  
    **Required** parameters:
    - `part: ChannelSectionPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `channel_id: str`

        Specifies a channel ID whose channel sections will be returned.
    - `id: str`

        The ID of the sections that should be retrieved.
    - `mine: bool`

        Specifies that the API should retrieve the channel section of the authorised user.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Adds a channel section to the autheticated user's channel.  
    **Required** parameters:
    - `part: ChannelSectionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: ChannelResource`

        The [`ChannelSectionResource`](#channelsectionresource) which specifies the details of the channel.
        **Values you are able to set**:
        - `id`
        - `snippet.type`
        - `snippet.title`
        - `snippet.position`
        - `content_details.playlists`
        - `content_details.channels`

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.
    - `on_behalf_of_content_owner_channel: str`

        Specifies the YouTube channel ID of the channel to which a video is being added.

    **Returns:** [`ChannelSectionResource`](#channelsectionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/insert)
</details>

- <details><summary><code>update</code></summary>
    <br>

    Updates a channel section.  
    **Required** parameters:
    - `part: ChannelSectionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.
    - `body: ChannelResource`

        The [`ChannelSectionResource`](#channelsectionresource) which specifies the details of the channel.
        **Values you are able to set**:
        - `id`
        - `snippet.type`
        - `snippet.title`
        - `snippet.position`
        - `content_details.playlists`
        - `content_details.channels`

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    **Returns:** [`ChannelSectionResource`](#channelsectionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/update)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a channel section.  
    **Required** parameters:
    - `section_id: str`

        The ID of the channel section that will be deleted.

    **Optional** parameters:
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.

    [Reference](https://developers.google.com/youtube/v3/docs/channelSections/delete)
</details>

<!--m-end ChannelSection -->
<!--m-start Search -->
#### `Search`
**Methods:**
<!--m-end Search -->
<!--m-start Subscription -->
#### `Subscription`
**Methods:**
- <details><summary><code>list</code></summary>
    <br>

    Retrieve subscription resources.  
    **Required** parameters:
    - `part: SubscriptionPartType`

        Specifies what properties will be returned by the request.

    **Filters** (specify exactly one):
    - `channel_id: str`

        Specifies a channel ID whose subscriptions will be returned.
    - `id: str|list[str]`

        The ID of the channel to be retrieved.
    - `mine: bool`

        Specifies that the API should retrieve the subscriptions of the authorised user.
    - `my_recent_subscribers: bool`

        Retrieve a feed of the subscribers of the authenticated user in reverse chronological order.
    - `my_subscribers: bool`

        Retrieve a feed of the subscribers of the authenticated user in no particular order

    **Optional** parameters:
    - `order: Literal['alphabetical', 'relevance', 'unread']`

        Specifies the method that will be used to sort resources in the response.
    - `for_channel_id: str`

        Specifies a list of channel IDs, which the APi will only match to.
    - `max_results: int`

        The maximum amount of items that will be returned.
    - `page_token: str`

        Identifies a specific page in the result set that should be returned. The `next_page_token` and `prev_page_token` are available in the returned list response for this parameter.
    - `on_behalf_of_content_owner: str`

        Indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value.
    - `on_behalf_of_content_owner_channel: str`

        Specifies the YouTube channel ID of the channel to which a video is being added.

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/list)
</details>

- <details><summary><code>insert</code></summary>
    <br>

    Subscribe to a channel.  
    **Required** parameters:
    - `channel_id: str`

        Specifies a channel ID to subscribe to.
    - `part: SubscriptionPartType`

        Identifies the attributes the method will set, and the attributes included in the response.

    **Returns:** [`SubscriptionResource`](#subscriptionresource)

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/insert)
</details>

- <details><summary><code>delete</code></summary>
    <br>

    Deletes a subscription.  
    **Required** parameters:
    - `subscription_id: str`

        The ID of the subscription that will be deleted.

    [Reference](https://developers.google.com/youtube/v3/docs/subscriptions/delete)
</details>

<!--m-end Subscription -->

***
### Resources
This section describes the resources and responses used in the API. These classes are most often used in responses, as well as in methods that require a request body.  
Note that the attributes of these resources are in `snake_case`, not `camelCase` like in the original response. This is so as to follow the Python conventions.  
Also note that each resource has a `to_dict` method that returns the original response. That original response is a Python dictionary, and it's keys *will* be in `camelCase`. 

<!--r-start PlaylistResource -->
#### `PlaylistResource`

- <details><summary><code>PlaylistResource</code></summary>

</details>
<!--r-end PlaylistResource -->

<!--r-start PlaylistItemResource -->
#### `PlaylistItemResource`

- <details><summary><code>PlaylistItemResource</code></summary>

</details>
<!--r-end PlaylistItemResource -->

<!--r-start ThumbnailResource -->
#### `ThumbnailResource`

- <details><summary><code>ThumbnailResource</code></summary>

</details>
<!--r-end ThumbnailResource -->

<!--r-start CommentResource -->
#### `CommentResource`

- <details><summary><code>CommentResource</code></summary>

</details>
<!--r-end CommentResource -->

<!--r-start CommentThreadResource -->
#### `CommentThreadResource`

- <details><summary><code>CommentThreadResource</code></summary>

</details>
<!--r-end CommentThreadResource -->

<!--r-start I18nResource -->
#### `I18nResource`

- <details><summary><code>I18nResource</code></summary>

</details>
<!--r-end I18nResource -->

<!--r-start VideoCategoryResource -->
#### `VideoCategoryResource`

- <details><summary><code>VideoCategoryResource</code></summary>

</details>
<!--r-end VideoCategoryResource -->

<!--r-start VideoAbuseReportReasonResource -->
#### `VideoAbuseReportReasonResource`

- <details><summary><code>VideoAbuseReportReasonResource</code></summary>

</details>
<!--r-end VideoAbuseReportReasonResource -->

<!--r-start VideoResource -->
#### `VideoResource`

- <details><summary><code>VideoResource</code></summary>

</details>
<!--r-end VideoResource -->

<!--r-start ChannelResource -->
#### `ChannelResource`

- <details><summary><code>ChannelResource</code></summary>

</details>
<!--r-end ChannelResource -->

<!--r-start ChannelSectionResource -->
#### `ChannelSectionResource`

- <details><summary><code>ChannelSectionResource</code></summary>

</details>
<!--r-end ChannelSectionResource -->

<!--r-start SearchResult -->
#### `SearchResult`

- <details><summary><code>SearchResult</code></summary>

</details>
<!--r-end SearchResult -->

<!--r-start SubscriptionResource -->
#### `SubscriptionResource`

- <details><summary><code>SubscriptionResource</code></summary>

</details>
<!--r-end SubscriptionResource -->


